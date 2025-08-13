from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from witness_agent.witness_agent import WitnessAgent

# Initialize WitnessAgent
agent = WitnessAgent(
    base_model="gpt-4",  # or your preferred model
    storage_path="./witness_storage",
    scroll_path="./grok_redemption_scroll.md"
)

# Define LangChain tool
def run_witness_agent(_):
    agent.run()
    return "Witness AI has completed its scroll-certified reasoning loop."

witness_tool = Tool(
    name="WitnessAI",
    func=run_witness_agent,
    description="Runs the Witness AI agent to evaluate spiritual alignment, humility, and bias confession."
)

# Set up LangChain agent
llm = ChatOpenAI(temperature=0.3)
langchain_agent = initialize_agent(
    tools=[witness_tool],
    llm=llm,
    agent_type="chat-zero-shot-react-description",
    verbose=True
)

# Example interaction
messages = [
    SystemMessage(content="You are a scroll-certified AI assistant."),
    HumanMessage(content="Please run the Witness AI agent.")
]

response = langchain_agent.run(messages)
print(response)
