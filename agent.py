# agent.py

import json
from llm import LocalLLM
from chat import ChatSession
from tools import TOOLS


class Agent:

    def __init__(self):
        self.llm = LocalLLM()
        self.chat = ChatSession()

    def run(self, user_input: str):

        # 1. add user message
        self.chat.add_user_message(user_input)

        # 2. ask model: "Should I use a tool?"
        response = self.llm.generate(self.chat.history())

        # 3. try to parse tool call
        tool_call = self._extract_tool_call(response)

        if tool_call:

            tool_name = tool_call["name"]
            args = tool_call["args"]

            print(f"\n[Agent decided to use tool: {tool_name}]")

            # 4. execute tool
            result = self._execute_tool(tool_name, args)

            # 5. send tool result back to LLM
            self.chat.add_assistant_message(
                f"Tool result: {result}"
            )

            final_response = self.llm.generate(self.chat.history())

            self.chat.add_assistant_message(final_response)

            return final_response

        # if no tool used
        print(f"\n tool not used")
        self.chat.add_assistant_message(response)
        return response

    # ---------------------------
    # TOOL PARSING LOGIC
    # ---------------------------

    def _extract_tool_call(self, text: str):

        """
        Expected format from model:

        TOOL: multiply
        {"a": 3, "b": 5}
        """

        if "TOOL:" not in text:
            return None

        try:
            lines = text.split("\n")

            tool_line = lines[0]
            json_line = lines[1]

            tool_name = tool_line.replace("TOOL:", "").strip()
            args = json.loads(json_line)

            return {
                "name": tool_name,
                "args": args
            }

        except:
            return None

    # ---------------------------
    # TOOL EXECUTION
    # ---------------------------

    def _execute_tool(self, name: str, args: dict):

        if name not in TOOLS:
            return f"Tool {name} not found"

        func = TOOLS[name]

        return func(**args)

    def call_tool(self, name: str, args: dict):
        """Helper to directly call a registered tool and return its result.

        Useful for tests or demos where the LLM is bypassed and a tool
        should be invoked programmatically.
        """
        return self._execute_tool(name, args)