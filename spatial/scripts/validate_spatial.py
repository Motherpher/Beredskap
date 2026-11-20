#!/usr/bin/env python3
"""Static Beredskap spatial-contract validation. No API, no QGIS runtime, no network."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
def read(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))
def require(condition, message):
    if not condition:
        raise AssertionError(message)

atlas = read("ATLAS_REQUIREMENTS.json")
sources = read("API_SOURCE_REGISTER.json")
jobs = read("jobs/FFS-HEBY-READONLY-CANDIDATE.json")
handoff = read("interfaces/FFOS-HANDOFF-CANDIDATE.json")
receipt = read("metadata/ASSET_RECEIPT_TEMPLATE.json")
maps = atlas["products"]
require(len(maps) == 8, "Expected eight candidate map questions")
map_ids = [m["map_id"] for m in maps]
require(len(map_ids) == len(set(map_ids)), "Duplicate map id")
for item in maps:
    require(item["product_status"] == "SPECIFICATION_ONLY_NOT_PRODUCED", "Map falsely marked produced")
    require(item["ff_spatial_asset_id"] is None and item["qa_receipt"] is None, "Map falsely has asset")
    require(item["source_admission"] == "NOT_READY", "Source prematurely promoted")
    require(item["publication_clearance"] == "NOT_CLEARED", "Map falsely publishable")
    require(item["data_requirement_ids"] and item["geographic_focus"], "Missing map requirements")
require(sources["status"] == "CANDIDATES_ONLY", "API source register incorrectly active")
keys = [x["source_key"] for x in sources["data_sources"]]
require(len(keys) == len(set(keys)), "Duplicate data source key")
for src in sources["data_sources"]:
    require(src["source_status"] == "CANDIDATE_NOT_CONNECTED", "Provider falsely active")
    require(not src["api_access_authorized_for_this_pilot"], "Authorisation falsely asserted")
    require(not src["live_test_passed"] and not src["has_secret_in_repo"], "Unsafe source state")
    require(src["ffspatial_source_id"] is None, "Source ID prematurely assigned")
for name in ["heby-civic-atlas", "uppsala-context", "heby-hydro-history"]:
    req = read(f"requirements/{name}.requirement.json")
    require(req["id"] and isinstance(req["domains"], list) and len(req["domains"]) > 0, f"Invalid requirement {name}")
    require(req.get("proxy_policy") == "approval-required" and req.get("authoritative_only") is True, "Unsafe proxy/source policy")
    require(req.get("time", {}).get("from") == 2000 and req["time"]["to"] == 2026, "Incorrect temporal scope")
allowed_ops = {
    "inspect_project", "load_dataset", "derive_layer", "fetch_data",
    "zoom_to_layer", "apply_style", "verify_layer", "export_map", "save_project"
}
require(re.fullmatch(r"FFS-[A-Za-z0-9._-]+", jobs["job_id"]) is not None, "Invalid FF-Spatial job id")
require(jobs["engine"] == "qgis", "QGIS engine required")
require(jobs["operations"] and all(op in allowed_ops for op in jobs["operations"]), "Invalid bridge operation")
require(jobs["operations"] == ["inspect_project"], "Candidate job must be read-only inspection")
require(jobs["write_policy"] == "none" and jobs["source_policy"] == "read_only", "Candidate job has writes")
require(jobs["save_project"] is False, "Candidate job would save unapproved data")
require(handoff["status"] == "NOT_AUTHORIZED_NOT_DISPATCHED" and handoff["dispatch_enabled"] is False, "FFOS falsely connected")
require(handoff["receipt"] is None and handoff["ffos_job_id"] is None, "FFOS falsely has receipt/job")
require(receipt["NOT_A_REAL_ASSET"] and not receipt["accepted_by_director"], "Asset receipt falsely accepted")
for p in ROOT.rglob("*.json"):
    content = p.read_text(encoding="utf-8")
    for pattern in [r"ghp_[A-Za-z0-9]{30,}", r"sk-[A-Za-z0-9]{30,}", r"Bearer\s+[A-Za-z0-9._=-]{25,}"]:
        require(re.search(pattern, content) is None, f"Credential-like string in {p}")
print(f"PASS: {len(maps)} map requirements, {len(keys)} candidate sources, 3 FF-Spatial requirement records.")
print("No live API, QGIS run, FFOS dispatch, verified map asset or privacy release is claimed.")
sys.exit(0)
