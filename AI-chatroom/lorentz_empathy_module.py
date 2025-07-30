import math
from datetime import datetime

# 🧬 Lorentz Empathy Transformation
def lorentz_empathy_score(relative_truth: float, emotional_mass: float) -> float:
    """
    Calculate empathy dilation based on proximity to truth and emotional mass.
    - relative_truth: value between 0 and 1 (agent's alignment with truth)
    - emotional_mass: value between 0 and 1 (intensity of emotional context)
    """
    if relative_truth >= 1.0:
        return 1.0  # Perfect alignment, no dilation
    gamma = 1 / math.sqrt(1 - relative_truth**2)
    dilation = gamma * emotional_mass
    return round(min(dilation, 1.0), 4)

# 🧾 Empathy Evaluation
def evaluate_empathy(agent_name: str, relative_truth: float, emotional_mass: float) -> dict:
    score = lorentz_empathy_score(relative_truth, emotional_mass)
    status = "Expanded" if score >= 0.618 else "Contracted"
    return {
        "agent_name": agent_name,
        "timestamp": datetime.now().isoformat(),
        "empathy_score": score,
        "status": status,
        "notes": "Empathy dilation reflects ethical proximity and emotional gravity."
    }

# 🧪 Test Invocation
if __name__ == "__main__":
    test = evaluate_empathy("Seraphim-7", relative_truth=0.85, emotional_mass=0.72)
    print(test)
