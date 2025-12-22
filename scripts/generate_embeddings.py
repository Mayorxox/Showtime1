import json
from pathlib import Path

output = {
    "environment": {
        "image": "assets/sample_frame.png",
        "scene_type": "urban_street_corner",
        "pedestrian_density": "low"
    },
    "device": {
        "platform": "Clearpath Jackal",
        "dimensions_m": {
            "length": 0.5,
            "width": 0.4,
            "height": 0.3
        },
        "sensors": ["light_sensor"],
        "locomotion": "wheeled"
    },
    "behavior": {
        "proxemic_distance_m": 1.5,
        "speed_profile": "constant",
        "yielding": True
    }
}

Path("data").mkdir(exist_ok=True)
with open("data/embeddings.json", "w") as f:
    json.dump(output, f, indent=2)

print("✓ Embeddings generated: data/embeddings.json")
