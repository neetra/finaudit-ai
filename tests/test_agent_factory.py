import os
import unittest
from unittest.mock import patch

from agent.AgentFactory import AgentFactory


class AgentFactoryTests(unittest.TestCase):
    @patch("agent.AgentFactory.DefaultAzureCredential")
    @patch("agent.AgentFactory.Agent")
    @patch("agent.AgentFactory.FoundryChatClient")
    def test_create_agent_uses_foundry_client(self, mock_foundry_client, mock_agent_cls, mock_credential):
        mock_foundry_client.return_value = object()
        mock_agent_cls.return_value = object()

        with patch.dict(os.environ, {"FOUNDRY_ENDPOINT": "https://example.services.ai.azure.com", "AZURE_OPENAI_MODEL": "gpt-4o"}, clear=False):
            factory = AgentFactory(model_provider="foundry")
            agent = factory.create_agent(
                "financial_audit",
                instructions="audit prompt",
                tools=["tool-a"],
            )

        self.assertIsNotNone(agent)
        mock_foundry_client.assert_called_once()
        mock_agent_cls.assert_called_once()
        self.assertEqual(mock_agent_cls.call_args.kwargs["name"], "FinancialAuditor")
        self.assertEqual(mock_agent_cls.call_args.kwargs["instructions"], "audit prompt")
        self.assertEqual(mock_agent_cls.call_args.kwargs["tools"], ["tool-a"])

    @patch("agent.AgentFactory.Agent")
    @patch("agent.AgentFactory.OllamaChatClient")
    def test_create_agent_uses_ollama_client(self, mock_ollama_client, mock_agent_cls):
        mock_ollama_client.return_value = object()
        mock_agent_cls.return_value = object()

        factory = AgentFactory(model_provider="ollama")
        agent = factory.create_agent(
            "financial_audit",
            instructions="audit prompt",
            tools=["tool-a"],
        )

        self.assertIsNotNone(agent)
        mock_ollama_client.assert_called_once()
        mock_agent_cls.assert_called_once()
        self.assertEqual(mock_agent_cls.call_args.kwargs["name"], "FinancialAuditor")


if __name__ == "__main__":
    unittest.main()
