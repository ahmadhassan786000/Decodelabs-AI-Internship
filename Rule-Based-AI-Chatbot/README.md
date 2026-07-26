# Rule-Based AI Chatbot

A simple rule-based chatbot built in Python. It uses a hardcoded dictionary of intents and responses to answer a small set of predefined questions and phrases.

## Features
- Handles greetings such as "hello"
- Handles farewells such as "bye"
- Responds to custom questions like:
  - what is your name
  - what can you do
  - who created you
- Supports an exit command: "exit"
- Returns the fallback message "I do not understand." for unknown input

## Project Structure
- app.py - Main entry point for the chat loop
- chatbot/ - Bot logic, knowledge base, and response handling
- tests/ - Simple test cases for the chatbot

## How to Run
1. Open the project folder:
   cd Rule-Based-AI-Chatbot
2. Activate the virtual environment:
   .venv\Scripts\Activate.ps1
3. Run the app:
   python app.py

## Example Inputs
- hello
- bye
- what is your name
- what can you do
- who created you
- random text
- exit

## Testing
Run the test suite with:

pytest -q
