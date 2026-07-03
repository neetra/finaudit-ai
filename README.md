# FinAudit AI - Personal Finance Analyzer
Upload statements. Track expenses. Get AI-powered financial insights.

# Description
- The AI Financial Audit Agent is an intelligent financial analysis platform that helps users understand their spending habits, savings, and overall financial health by analyzing bank statements, credit card statements, and other financial documents.
- Instead of simply answering questions, the agent acts like a virtual financial analyst. It extracts financial information, categorizes transactions, identifies trends, detects unusual spending patterns, and generates personalized financial insights and recommendations.
- The project is being developed incrementally to demonstrate how a production-grade AI agent evolves from a simple LLM integration into a scalable, cloud-native, multi-agent platform.

# Project Setup

## 1. Create a virtual environment
- On Windows:
  - `python -m venv .venv`
  - `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
  - `.\.venv\Scripts\Activate.ps1`
- On macOS/Linux:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`

## 2. Install requirements
- `pip install -r requirements.txt`

## 2.5. Entry file
- The main application entry point is `main.py`.
- Start the app with:
  - `python main.py`

## 3. Configure environment variables
- Copy or create the `.env` file in the project root.
- Use `MODEL_PROVIDER` to select which model provider the agent uses.
- Supported values in this project may include:
  - `ollama`
  - `openai`
  

## 4. Model options
The project supports either locally deployed models or cloud models.

### Local model setup (Ollama)
- Install Ollama locally from https://ollama.com/docs/install.
- Start the Ollama daemon and deploy a model:
  - `ollama install gemma4`
  - `ollama serve gemma4`
- Confirm the model is running.
- Set `.env` values:
  - `MODEL_PROVIDER=ollama`
  - `OLLAMA_MODEL=gemma4`
- In the code, choose the `ollama` provider when initializing the agent.

### Cloud model setup (OpenAI)
- Sign up for OpenAI and create an API key.
- Set `.env` values:
  - `OPENAI_API_KEY=sk-...`
  - `OPENAI_MODEL=gpt-5`
  - `MODEL_PROVIDER=openai`
- Ensure the `openai` provider is selected in the agent configuration.

# References
- Ollama Documentation
- OpenAI API Documentation
- https://linkedin.com/learning/building-ai-agents-for-beginners-by-microsoft
- https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/?practice-assessment-type=certification
- https://microsoft.github.io/ai-agents-for-beginners/
