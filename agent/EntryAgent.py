from agent.agent import BaseAgent


class EntryAgent(BaseAgent):
    """Simple entrypoint agent that handles initial user interaction."""

    def __init__(self, model_provider: str, agent_name: str = "entry_agent", instructions: str = None, tools: list = None):
        super().__init__(model_provider=model_provider, agent_name=agent_name, instructions=instructions, tools=tools)

    def process(self, user_input: str):
        return self.run(user_input)
