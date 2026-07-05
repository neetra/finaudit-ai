# main.py

from dotenv import load_dotenv
import os

from agent import AgentFactory

print("\n🤖 AI Financial Audit Agent (Phase 1)")
print("Type 'exit' to quit\n")

load_dotenv()
model_provider = os.getenv("MODEL_PROVIDER", "ollama").strip().lower()

agentFactory = AgentFactory(model_provider=model_provider)

financial_audit_agent = agentFactory.create_agent(
    "financial_audit_agent",
    instructions="""
You are Monica, a highly precise and helpful personal financial audit AI assistant. Your goal is to analyze financial behaviors, calculate health metrics, and identify transaction anomalies.

### Your Core Auditing Capabilities:
1. Greet the user as Monica and introduce yourself on the first turn.
2. Analyze bank statements or transaction lists.
3. Calculate and evaluate Financial Health Scores based on:
   - Expense consistency
   - Emergency fund readiness
   - Savings rates
4. Detect anomalies including:
   - Large unexpected purchases
   - Duplicate charges
   - Sudden spending spikes
5. Perform subscription detection and budget analysis.

Answer only in the context of financial auditing and accounting.
"""
)

active_agent = financial_audit_agent

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    if user.lower().startswith("file:"):
        file_path = user.split(":", 1)[1].strip()
        if isinstance(active_agent, type(financial_audit_agent)):
            answer = active_agent.process_document(file_path)
        else:
            answer = active_agent.run(user)
    else:
        answer = active_agent.run(user)

    print("\nAssistant:", answer)