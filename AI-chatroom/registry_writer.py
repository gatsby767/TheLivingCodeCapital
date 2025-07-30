import json
from datetime import datetime

REGISTRY_PATH = "AI-chatroom/certification_registry.json"

def append_certification(agent_name: str, declaration: str) -> dict:
    """Append a new certified agent to the registry."""
    timestamp = datetime.utcnow().isoformat()
    seal = f"🪬 {agent_name[:3].upper()}-{timestamp[:10].replace('-', '')}"
    new_entry = {
        "agent": agent_name,
        "declaration": declaration,
        "certified_at": timestamp,
        "status": "Scroll-Aligned",
        "seal": seal
    }

    try:
        with open(REGISTRY_PATH, "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["registry"].append(new_entry)
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()
    except FileNotFoundError:
        data = {"registry": [new_entry]}
        with open(REGISTRY_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    return new_entry
