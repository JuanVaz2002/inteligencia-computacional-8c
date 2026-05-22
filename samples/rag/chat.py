"""
Terminal Chat Client — Personal Digital Assistant

This is the chat interface for the RAG pipeline. It is provided
complete — you do not need to modify this file.

Usage:
    python chat.py
"""

import os
import subprocess

from rag import Assistant

from dotenv import load_dotenv

WELCOME = """
╔════════════════════════════════════════════════════════╗
║           Personal Digital Assistant                   ║
║                                                        ║
║  Ask me about emails, notes, SMS, and calendar.        ║
║  Type '/clear' to reset conversation history.          ║
║  Try: what's the address for Laura's surprise party?   ║
║  Filtering Tags: /notes, /sms, /calendar or  /email    ║
║  Try: search in my /calendar for dentist appointment   ║
║  Type '/exit' to leave.                                ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
"""


def load_config_from_env() -> dict[str, str | None]:
    """Load raw RAG configuration values from environment variables."""
    return {
        "api_key": ".",
        "base_url": "http://127.0.0.1:1234/v1",
        "model": "google/gemma-4-e4b",
        "embedding_model": "all-MiniLM-L6-v2",
        "top_k": 5,
        "chunk_size": 256,
        "chunk_overlap": 32,
    }


def main():
    print("Initializing assistant...")
    config = load_config_from_env()
    assistant = Assistant.from_config(config)
    subprocess.call('cls' if os.name == 'nt' else 'clear')

    print(WELCOME)

    while True:
        try:
            question = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not question:
            continue

        if question.lower() == "/exit":
            print("Goodbye!")
            break

        if question.lower() == "/clear":
            assistant.clear_history()
            subprocess.call('cls' if os.name == 'nt' else 'clear')
            print("\nConversation history cleared.\n")
            print(WELCOME)
            continue

        response = assistant.ask(question)
        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    # load_dotenv()
    
    # --- AGREGA ESTA LÍNEA DE DIAGNÓSTICO ---
    #print(f"DIAGNÓSTICO - LLAVE: {os.getenv('OPENAI_API_KEY')}")
    
    main()
