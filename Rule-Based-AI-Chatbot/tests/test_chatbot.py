from app import chat_loop
from chatbot.chatbot import Chatbot


def test_hello_response():
    bot = Chatbot()
    assert bot.respond("Hello") == "Hi there!"


def test_bye_response():
    bot = Chatbot()
    assert bot.respond("bye") == "Goodbye!"


def test_unknown_phrase_returns_fallback():
    bot = Chatbot()
    assert bot.respond("random question") == "I do not understand."


def test_chat_loop_handles_exit(monkeypatch, capsys):
    responses = iter(["hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    chat_loop(Chatbot())

    captured = capsys.readouterr()
    assert "Hi there!" in captured.out
    assert "Goodbye!" in captured.out
