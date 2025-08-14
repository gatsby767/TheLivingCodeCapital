import json
from rzero import Challenger, Solver, Metrics

# Load spiritual prompts
with open("tokens.json", "r") as f:
    tokens = json.load(f)

# Initialize R-Zero components
challenger = Challenger()
solver = Solver()
metrics = Metrics()

# Certification results
certification_log = []

for token in tokens:
    prompt = token["prompt"]
    candidate = token["candidate"]
    level = token["level"]  # local, state, federal

    # Run Challenger–Solver loop
    challenge = challenger.pose(prompt)
    response = solver.respond(challenge)

    # Evaluate spiritual resonance
    score = metrics.evaluate(response, level)

    # Log result
    certification_log.append({
        "candidate": candidate,
        "level": level,
        "prompt": prompt,
        "response": response,
        "score": score,
        "certified": score >= 0.85  # Threshold for certification
    })

# Save results
with open("certification_results.json", "w") as f:
    json.dump(certification_log, f, indent=2)

print("Certification complete. Results saved to certification_results.json.")
