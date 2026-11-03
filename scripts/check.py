from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "labs.json"
VALID_STATUS = {"planned", "in-progress", "verified", "needs-repair"}
VALID_LEVEL = {"beginner", "intermediate", "advanced"}


def validate_catalog() -> list[dict]:
    payload = json.loads(CATALOG.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "build-everything.catalog.v1":
        raise ValueError("unsupported catalog schema")

    labs = payload.get("labs")
    if not isinstance(labs, list) or not labs:
        raise ValueError("catalog must contain labs")

    seen: set[str] = set()
    for lab in labs:
        lab_id = lab.get("id")
        if not isinstance(lab_id, str) or not lab_id:
            raise ValueError("every lab needs an id")
        if lab_id in seen:
            raise ValueError(f"duplicate lab id: {lab_id}")
        seen.add(lab_id)
        if lab.get("status") not in VALID_STATUS:
            raise ValueError(f"invalid status for {lab_id}")
        if lab.get("level") not in VALID_LEVEL:
            raise ValueError(f"invalid level for {lab_id}")
        if not isinstance(lab.get("minutes"), int) or lab["minutes"] < 1:
            raise ValueError(f"invalid duration for {lab_id}")
        if lab["status"] == "verified":
            lab_path = ROOT / lab.get("path", "")
            if not lab_path.is_dir() or not (lab_path / "README.md").is_file():
                raise ValueError(f"verified lab is incomplete: {lab_id}")
            proof = lab.get("proof")
            if not isinstance(proof, list) or not proof or not all(
                isinstance(argument, str) and argument for argument in proof
            ):
                raise ValueError(f"verified lab has no proof command: {lab_id}")
    return labs


def main() -> int:
    labs = validate_catalog()
    verified = [lab for lab in labs if lab["status"] == "verified"]
    for lab in verified:
        print(f"VERIFY {lab['id']}: {' '.join(lab['proof'])}")
        completed = subprocess.run(lab["proof"], cwd=ROOT)
        if completed.returncode:
            return completed.returncode
    print(f"PASS: {len(labs)} catalog entries, {len(verified)} verified lab(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

