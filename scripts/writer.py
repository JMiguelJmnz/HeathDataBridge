import os
import json
from pathlib import Path

def write_resource(resource, filename):
    # Find project root
    project_root = Path(__file__).resolve().parents[1]

    # Building output path
    path = project_root / "output" / "fhir" / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
        f.write(resource.model_dump_json(indent=2))
