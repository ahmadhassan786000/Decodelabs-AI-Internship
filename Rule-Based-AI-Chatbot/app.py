from chatbot.chatbot import Chatbot


def chat_loop(bot: Chatbot) -> None:
    print("Rule-Based AI Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        cleaned = user_input.strip().lower()

        if cleaned in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break

        response = bot.respond(cleaned)
        print(f"Bot: {response}")


def main() -> None:
    chat_loop(Chatbot())


if __name__ == "__main__":
    main()
