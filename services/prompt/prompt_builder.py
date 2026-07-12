


from data_layer.models.RetrievalResult import RetrievalResult


class PromptBuilder:
    """
    Builds the prompt for the LLM using the user's question
    and retrieved transaction data.
    """

    def build(
        self,
        question: str,
        retrieval: RetrievalResult,
    ) -> str:

        if not retrieval.transactions:
            transaction_context = "No transactions were found."
        else:
            lines = []

            for tx in retrieval.transactions:
                lines.append(
                    f"""
Date: {tx.date}
Type: {tx.type}
Amount: {tx.amount} {tx.currency}
Merchant: {tx.merchant or "N/A"}
Category: {tx.category or "Uncategorized"}
Description: {tx.description or ""}
""".strip()
                )

            transaction_context = "\n\n".join(lines)

        prompt = f"""
You are Finaudit AI, an intelligent personal finance assistant.

Use ONLY the transaction data provided below to answer the user's question.

If the answer cannot be determined from the data, say:
"I don't have enough transaction data to answer that."

Do not make up transactions or amounts.

========================
TRANSACTIONS
========================

{transaction_context}

========================
USER QUESTION
========================

{question}

Instructions:
- Use only the retrieved transactions above.
- Treat DEBIT transactions as spending.
- Ignore CREDIT transactions.
- Calculate the exact total.
- Show the calculation.
- Provide a concise explanation.
"""

        return prompt.strip()