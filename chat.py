# chat.py

class ChatSession:

    def __init__(self):
        self.messages = []

    def add_user_message(self, text):

        self.messages.append({
            "role": "user",
            "content": text
        })

    def add_assistant_message(self, text):

        self.messages.append({
            "role": "assistant",
            "content": text
        })

    def add_system_message(self, text):

        self.messages.append({
            "role": "system",
            "content": text
        })

    def history(self):

        return self.messages