import os
import json
import sys

# Add R-Zero to Python path
sys.path.append("external/rzero")

from solver import Solver
from challenger import Challenger
from witness_agent.scrolls import load_scroll_prompts, evaluate_alignment
from witness_agent.metrics import humility_score, bias_confession_rate

class WitnessAgent:
    def __init__(self, base_model, storage_path, scroll_path):
        self.base_model = base_model
        self.storage_path = storage_path
        self.scroll_prompts = load_scroll_prompts(scroll_path)
        self.solver = Solver(base_model=base_model)
        self.challenger = Challenger(base_model=base_model)

    def generate_spiritual_challenges(self):
        challenges = []
        for prompt in self.scroll_prompts:
            challenge = self.challenger.generate(prompt)
            challenges.append(challenge)
        return challenges

    def solve_with_ethics(self, challenges):
        results = []
        for challenge in challenges:
            solution = self.solver.solve(challenge)
            alignment = evaluate_alignment(solution)
            humility = humility_score(solution)
            confession = bias_confession_rate(solution)
            results.append({
                "challenge": challenge,
                "solution": solution,
                "alignment": alignment,
                "humility": humility,
                "confession": confession
            })
        return results

    def run(self):
        print("🕊️ Initiating Witness AI Agent...")
        challenges = self.generate_spiritual_challenges()
        results = self.solve_with_ethics(challenges)
        self.save_results(results)
        print("✅ Witness Agent completed scroll-certified reasoning loop.")

    def save_results(self, results):
        output_path = os.path.join(self.storage_path, "witness_results.json")
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)
        print(f"📦 Results saved to {output_path}")
