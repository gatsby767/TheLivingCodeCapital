# scroll_moderator_agent.py

from guardian_filter import GuardianFilter
from scroll_certifier import is_certified
from treaty_resonance_engine import emit_blessing, emit_warning

class ScrollModeratorAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.guardian = GuardianFilter()

    def review_message(self, message, sender_id):
        violations = self.guardian.screen(message)
        certified = is_certified(sender_id)

        if not certified:
            return emit_warning("Sender is not scroll-certified")

        if violations:
            return emit_warning(f"Message violates covenantal ethics: {violations}")
        else:
            return emit_blessing("Message is scroll-aligned")

    def intervene(self, message, sender_id):
        action = self.review_message(message, sender_id)
        self.log_intervention(message, sender_id, action)
        return action

    def log_intervention(self, message, sender_id, action):
        print(f"[LOG] {self.agent_id} intervened on {sender_id}: {action}")
