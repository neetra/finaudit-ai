# main.py

from agent import Agent

agent = Agent()

SYSTEM_PROMPT = """
You are an AI agent.

If you need a tool, respond ONLY in this format:

TOOL: tool_name
{"arg1": value, "arg2": value}

Available tools:
- add(a, b)
- multiply(a, b)
- get_weather(city)

If no tool is needed, answer normally.
"""

agent.chat.add_user_message(SYSTEM_PROMPT)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    answer = agent.run(user)

    print("\nAssistant:", answer)