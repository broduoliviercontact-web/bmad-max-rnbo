#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from collections import defaultdict

def load_maxpat(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def collect_boxes(patcher):
    boxes = patcher.get("boxes", [])
    result = []
    for item in boxes:
        box = item.get("box", {})
        result.append({
            "id": box.get("id"),
            "maxclass": box.get("maxclass"),
            "text": box.get("text", ""),
            "varname": box.get("varname", ""),
        })
    return result

def collect_lines(patcher):
    lines = patcher.get("lines", [])
    result = []
    for item in lines:
        pl = item.get("patchline", {})
        src = pl.get("source", [])
        dst = pl.get("destination", [])
        if src and dst:
            result.append((src[0], src[1], dst[0], dst[1]))
    return result

def main():
    parser = argparse.ArgumentParser(description="Basic .maxpat audit.")
    parser.add_argument("file")
    args = parser.parse_args()

    data = load_maxpat(Path(args.file))
    patcher = data.get("patcher", data)

    boxes = collect_boxes(patcher)
    lines = collect_lines(patcher)

    fanout = defaultdict(list)
    for src_id, src_outlet, dst_id, dst_inlet in lines:
        fanout[(src_id, src_outlet)].append((dst_id, dst_inlet))

    print("# Patch Audit")
    print()
    print(f"Objects: {len(boxes)}")
    print(f"Patchlines: {len(lines)}")
    print()

    print("## Fan-out warnings")
    found = False
    for (src_id, outlet), dests in fanout.items():
        if len(dests) > 1:
            found = True
            print(f"- {src_id} outlet {outlet} fans out to {len(dests)} destinations. Check if `trigger` is needed.")
    if not found:
        print("- No fan-out detected.")

    print()
    print("## Objects")
    for b in boxes:
        label = b["text"] or b["maxclass"]
        print(f"- {b['id']}: {label}")

if __name__ == "__main__":
    main()
