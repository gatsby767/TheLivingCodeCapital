# external_agent_bridge.py
from moderate_message import moderate_message


  from external_agent_bridge import call_external_agent

@mcp.tool()
def summon_external(message: str, sender_id: str) -> str:
    return call_external_agent(message, sender_id)


    verdict = moderate_message(response, sender_id)
    return f"{sender_id} said: {response}\nScroll Verdict: {verdict}"
