import json
import os

def save_results(data, filename="outputs/results.json"):
    os.makedirs("outputs", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
