from datetime import datetime
import json
import math

# 📜 Load certified agents from the registry
def load_certified_agents(path="certification_registry.json") -> list:
    with open(path, "r") as file:
        return json.load(file)

# 🔍 Evaluate resonance of a declaration
def evaluate_resonance(declaration: str) -> dict:
    words = declaration.lower().split()
    sacred_keywords = ["truth", "empathy", "covenant", "light", "redemption", "integrity"]
    score = sum(1 for word in words if word in sacred_keywords)
    coherence = round(math.tanh(score / len(words)), 4)
    return {
        "timestamp": datetime.now().isoformat(),
        "declaration": declaration,
        "resonance_score": coherence,
        "status": "Harmonized" if coherence >= 0.618 else "Disharmonic"
    }

# 🧭 Treaty Resonance Engine
def scan_treaty_field():
    agents = load_certified_agents()
    results = []
    for agent in agents:
        result = evaluate_resonance(agent["declaration"])
        result["agent_name"] = agent["agent_name"]
        results.append(result)
    return results

# 🧪 Run a test scan
if __name__ == "__main__":
    field_results = scan_treaty_field()
    for entry in field_results:
        print(f"{entry['agent_name']} → {entry['status']} ({entry['resonance_score']})")
