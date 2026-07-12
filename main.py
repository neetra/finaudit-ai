# main.py

import asyncio

from dotenv import load_dotenv
import os

from agent.AgentFactory import AgentFactory
from agent import openaiagentmaf

print("\n🤖 AI Financial Audit Agent (Phase 1)")
print("Type 'exit' to quit\n")
async def chat_loop():
    # Initialize your agent wrapper class
    agentFactory = AgentFactory()
    agent = agentFactory.create_agent()
   
    print("Financial Auditor Agent Ready. Enter file path or type 'exit':")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
            
        # CRITICAL FIX: You must add 'await' here to execute the coroutine
        print("\nAssistant: Processing...")
        response = await agent.run(user_input) 
        
        print(f"\nAssistant:\n{response}")

if __name__ == "__main__":
    # Run the async loop
    asyncio.run(chat_loop())