# agent.py

import json
from llms.factory import LLMFactory
#from llms.ollama_llm import LocalLLM
from chat import ChatSession
from tools import TOOLS


class Agent:

    def __init__(self, model_name = "ollama"):
        self.llm = LLMFactory.create(model_name)
        self.chat = ChatSession()

    def run(self, user_input: str):

        self.chat.add_user_message(user_input)

        response = self.llm.generate(self.chat.history())

       
        tool_decision = self._parse_json(response)

        if tool_decision is None:
            self.chat.add_assistant_message(f"Tool decision: {response}")
            return response

        tool_name = tool_decision.get("tool", None)
        args = tool_decision.get("args", None)

        # CASE 1: no tool needed
        if tool_name is None:
            answer = tool_decision.get("answer")
          
            self.chat.add_assistant_message(f"Tool decision: {answer}")
            return answer

        print(f"\n[Using tool: {tool_name}]")

        # CASE 2: execute tool
        result = self._execute_tool(tool_name, args)

        # feed result back to model
        
        self.chat.add_assistant_message(
            f"Tool result: {result}"
        )

        

        return f"Answer is {result}"

    # ----------------------

    def _parse_json(self, text: str):

        try:
            
            return json.loads(text)
        except:
            print(f"Failed to parse JSON: {text}")
            return None

    # ----------------------

    def _execute_tool(self, name, args):

        if name not in TOOLS:
            return f"Tool {name} not found"

        return TOOLS[name](**args)  