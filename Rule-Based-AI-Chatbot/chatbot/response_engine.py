from .knowledge_base import INTENTS


def get_response(user_input: str) -> str:
    return INTENTS.get(user_input, "I do not understand.")
