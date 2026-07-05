from __future__ import annotations

from typing import Any, Optional, Sequence

from agent.EntryAgent import EntryAgent
from agent.FinancialAuditAgent import FinancialAuditAgent


class AgentFactory:
    """Create configured agent instances for the application."""

    def __init__(self, model_provider: Optional[str] = None):
        self.model_provider = model_provider or "ollama"

    def create_agent(
        self,
        agent_name: str,
        instructions: Optional[str] = None,
        tools: Optional[Sequence[Any]] = None,
        **kwargs: Any,
    ):
        if agent_name == "financial_audit_agent":
            return FinancialAuditAgent(
                model_provider=self.model_provider,
                agent_name=agent_name,
                instructions=instructions,
                tools=list(tools or []),
                **kwargs,
            )

        return EntryAgent(
            model_provider=self.model_provider,
            agent_name=agent_name,
            instructions=instructions,
            tools=list(tools or []),
            **kwargs,
        )
