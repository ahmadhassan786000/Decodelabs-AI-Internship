from .processor import clean_input
from .response_engine import get_response


class Chatbot:
    def __init__(self):
        self.name = "Rule-Based AI Chatbot"

    def respond(self, user_input: str) -> str:
        cleaned = clean_input(user_input)
        return get_response(cleaned)
