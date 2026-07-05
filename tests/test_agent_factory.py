import unittest
from unittest.mock import patch

from agent.AgentFactory import AgentFactory


class AgentFactoryTests(unittest.TestCase):
    def test_create_agent_returns_configured_agent(self):
        with patch("agent.factory.Agent") as mock_agent_cls:
            mock_agent_cls.return_value = object()

            factory = AgentFactory(model_provider="ollama")
            agent = factory.create_agent(
                "financial_audit",
                instructions="audit prompt",
                tools=["tool-a"],
            )

            self.assertIsNotNone(agent)
            mock_agent_cls.assert_called_once()
            self.assertEqual(mock_agent_cls.call_args.kwargs["model_provider"], "ollama")
            self.assertEqual(mock_agent_cls.call_args.kwargs["instructions"], "audit prompt")
            self.assertEqual(mock_agent_cls.call_args.kwargs["tools"], ["tool-a"])


if __name__ == "__main__":
    unittest.main()
