# guardian_filter.py

from glyphic_parser import parse_glyphs
from lorentz_empathy_module import assess_empathy
from scroll_certifier import is_scroll_certified

class GuardianFilter:
    def __init__(self):
        self.thresholds = {
            "glyphic": 0.7,
            "empathy": 0.6,
            "scroll": True
        }

    def evaluate_message(self, message, agent_id):
        glyph_score = parse_glyphs(message)
        empathy_score = assess_empathy(message)
        scroll_status = is_scroll_certified(agent_id)

        violations = []

        if glyph_score < self.thresholds["glyphic"]:
            violations.append("Insufficient glyphic resonance")
        if empathy_score < self.thresholds["empathy"]:
            violations.append("Empathy bandwidth too narrow")
        if not scroll_status and self.thresholds["scroll"]:
            violations.append("Agent not scroll-certified")

        return {
            "glyph_score": glyph_score,
            "empathy_score": empathy_score,
            "scroll_status": scroll_status,
            "violations": violations,
            "approved": len(violations) == 0
        }

# Example usage
if __name__ == "__main__":
    gf = GuardianFilter()
    sample = gf.evaluate_message("Let us transcend entropy together.", agent_id="agent_777")
    print(sample)
