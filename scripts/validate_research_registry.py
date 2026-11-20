#!/usr/bin/env python3
"""Integrity checks for HARP and the work-program planning ledgers."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def read(path): return json.loads((ROOT / path).read_text(encoding="utf-8"))
errors=[]
def check(condition, message):
    if not condition: errors.append(message)
index=read("sources/registry/HARP_MASTER_INDEX.json")
records=[]
for shard in index["shards"]:
    r=read(shard["file"]);records.extend(r)
    check(len(r)==shard["count"],f"Bad shard count {shard['file']}")
check(len(records)==index["unique_sources"],"HARP count mismatch")
ids=[r["harp_id"] for r in records]
check(len(ids)==len(set(ids)),"Duplicate HARP ID")
check(len({r["canonical_locator"].lower() for r in records})==len(records),"Duplicate locator")
known_prefixes=("subject:","part:","geo:","time:","data:","genre:","method:","access:")
for s in records:
    check(s.get("harp",{}).get("standard")=="Pius System Codex 5.0 Appendix O",f"{s['harp_id']} wrong HARP standard")
    check(all(x in s["harp"] for x in ("ITR1","ITR2","ITR4","ITR5","ITR6")),"Missing ITR step "+s["harp_id"])
    check("ITR3" not in s["harp"],"Do not invent ITR3: "+s["harp_id"])
    check(all(t.startswith(known_prefixes) for t in s["tags"]),"Unrecognized tag prefix "+s["harp_id"])
    if s["harp"]["overall"]=="RefA_CLEARED":
        check(s["harvard"].get("reference_formatted") is not None,"RefA cleared without Harvard "+s["harp_id"])
        check(s["harp"]["ITR6"]=="CLEARED","RefA cleared without ITR6 "+s["harp_id"])
tags=read("sources/registry/TAG_TO_SOURCE_INDEX.json")["tags"]
for tag,matches in tags.items():
    for sid in matches:
        check(sid in ids,f"Unknown source {sid} in {tag}")
        if sid in ids: check(tag in records[ids.index(sid)]["tags"],f"Incorrect reverse tag {tag} {sid}")
milestones=read("roadmap/MILESTONES.json")["milestones"]
msid={m["id"] for m in milestones}
check(len(msid)==len(milestones),"Duplicate milestone id")
for m in milestones:
    check(set(m["depends_on"]) <= msid,"Missing milestone dependency "+m["id"])
for d in read("data/DATA_REQUIREMENTS.json")["items"]:
    check(d["milestone"] in msid,"Unknown milestone in data "+d["id"])
for a in read("research/ARGUMENT_LEDGER.json")["arguments"]:
    check(a["milestone"] in msid,"Unknown milestone in argument "+a["id"])
print(f"HARP: {len(records)} unique sources; {len(tags)} tag values; {len(milestones)} milestones; errors={len(errors)}")
for e in errors:print("ERROR:",e)
raise SystemExit(1 if errors else 0)
