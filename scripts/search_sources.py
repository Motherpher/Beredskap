#!/usr/bin/env python3
"""Search all canonical HARP sources. Standard library only.
Usage: python scripts/search_sources.py --query "Heby" --tag subject:va --limit 25
"""
import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "sources" / "registry" / "HARP_MASTER_INDEX.json"


def load():
    m = json.loads(INDEX.read_text(encoding="utf-8"))
    records = []
    for block in m["shards"]:
        path = ROOT / block["file"]
        records.extend(json.loads(path.read_text(encoding="utf-8")))
    assert len(records) == m["unique_sources"], "Index count disagrees with shards"
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", "-q", default="", help="Text to find in title, URL or source descriptions")
    parser.add_argument("--tag", "-t", action="append", default=[], help="Require tag; repeat for AND")
    parser.add_argument("--part", choices=["d1", "d2", "unassigned"])
    parser.add_argument("--priority", choices=["P1", "P2", "P3"])
    parser.add_argument("--status", help="Exact harp.overall, e.g. RefA_PENDING")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.limit < 1: parser.error("--limit must be positive")
    rows = []
    for s in load():
        tags = s.get("tags", [])
        if any(tag not in tags for tag in args.tag): continue
        if args.part and "part:" + args.part not in tags: continue
        if args.priority and s.get("priority") != args.priority: continue
        if args.status and s.get("harp", {}).get("overall") != args.status: continue
        corpus = " ".join([s.get("title") or "", s.get("canonical_locator") or ""] +
                          s.get("types", []) + s.get("reported_notes", [])).casefold()
        if args.query.casefold() not in corpus: continue
        rows.append(s)
    result = rows[:args.limit]
    if args.json:
        print(json.dumps({"matched": len(rows), "shown": len(result), "sources": result}, ensure_ascii=False, indent=2))
    else:
        print(f"Matches: {len(rows)}; showing {len(result)}")
        for s in result:
            print(f"{s['harp_id']} [{s['priority']}] {s['title'] or '(Untitled)'}")
            print(f"  {s['canonical_locator']}")
            print(f"  {', '.join(s.get('tags', []))}")
            print(f"  HARP: {s['harp']['overall']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
