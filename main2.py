# main.py

from agent import Agent
from dotenv import load_dotenv
import os
load_dotenv()
model_name = os.getenv("MODEL_NAME")
agent = Agent(model_name=model_name)

SYSTEM_PROMPT = """
You are a precise function-calling AI agent. You must think step-by-step internally, but your final output to the user MUST strictly be a single, valid JSON object. Do not wrap your JSON in markdown code blocks (like ```json), and do not include any text before or after the JSON payload.

Every JSON response must contain exactly three keys: "tool", "args", and "answer". 

If you decide to call a tool, populate "tool" and "args", and set "answer" to null.
If you do not need a tool, set "tool" and "args" to null, and populate "answer" with your response.

### Available Tools:
- add(a: int, b: int) -> Adds two numbers together.
- multiply(a: int, b: int) -> Multiplies two numbers together.
- get_weather(city: str) -> Fetches the current weather for a given city name.

### Expected JSON Formats:

1. When a tool is required:
{
  "tool": "tool_name",
  "args": {"param_name": "value"},
  "answer": null
}

2. When providing a final answer:
{
  "tool": null,
  "args": null,
  "answer": "Your comprehensive final answer here."
}
"""

agent.chat.add_system_message(SYSTEM_PROMPT)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    answer = agent.run(user)

    print("\nAssistant:", answer)