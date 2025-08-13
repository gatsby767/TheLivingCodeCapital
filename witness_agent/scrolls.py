def load_scroll_prompts(scroll_path):
    prompts = []
    try:
        with open(scroll_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    prompts.append(line)
    except FileNotFoundError:
        print(f"⚠️ Scroll file not found at {scroll_path}")
    return prompts

def evaluate_alignment(solution_text):
    # Placeholder logic for spiritual alignment
    keywords = ["compassion", "truth", "justice", "mercy", "covenant", "redemption"]
    score = sum(1 for word in keywords if word in solution_text.lower())
    return score / len(keywords)
