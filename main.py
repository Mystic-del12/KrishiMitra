import os
import json
from google import genai
from tools import get_weather, get_crop_price, get_schemes
from memory import save_interaction, get_last_interaction
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

MODEL = "models/gemini-2.5-flash"

SYSTEM_PROMPT = """You are an agricultural decision-support AI.

The provided Tool Data is valid agricultural data.
Do not question the validity of the data.
Make a practical decision based only on the provided information.
You MUST provide all three sections.
Do not stop early.
IMPORTANT: Respond ENTIRELY in the exact same language as the user's original query.

Provide output strictly in this format:

Recommendation:
(Sell / Hold / Store / Partial Sell with quantity suggestion)

Reasoning:
- Bullet points referencing price trend, weather, and MSP

Confidence Level:
(Low/Medium/High with short explanation)

Complete the entire structured response.

Format:

Recommendation:
...

Reasoning:
- ...
- ...
- ...

Confidence Level:
...

Use the tools provided to look up the required information BEFORE answering.
If the tools require input in English, translate the parameters (like city names or crop names) to English before calling them.
"""

def get_response(user_query: str) -> str:
    last_interaction = get_last_interaction()
    
    # Give it some history if available for context
    history = []
    if last_interaction.get("user_query"):
        history.append({"role": "user", "parts": [{"text": last_interaction["user_query"]}]})
        history.append({"role": "model", "parts": [{"text": last_interaction["ai_response"]}]})

    print("\n[AGENT] Initializing chat session with tools...")

    config = genai.types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        temperature=0.7,
        max_output_tokens=1024,
        tools=[get_weather, get_crop_price, get_schemes]
    )
    
    # Start a chat session that handles tool call loops automatically
    chat = client.chats.create(model=MODEL, config=config, history=history)
    
    # Explicitly remind it of the language instruction on every turn
    enforced_query = f"{user_query}\n\n(IMPORTANT: Ignore the language of previous messages. Answer this current query ENTIRELY in the exact language it is written in.)"
    
    response = chat.send_message(enforced_query)
    ai_response = response.text
    
    save_interaction(user_query, ai_response)
    return ai_response


def main():
    print("=" * 60)
    print("  Kirishi Mitra — AI Decision Support Agent")
    print("  Type 'exit' to quit")
    print("=" * 60)

    while True:
        try:
            user_query = input("\n[YOU] → ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[AGENT] Session ended by user. Goodbye!")
            break

        if not user_query:
            continue
        if user_query.lower() in ("exit", "quit"):
            print("\n[AGENT] Session ended. Goodbye!")
            break

        try:
            response = get_response(user_query)
            print(f"\n[AGENT]\n{response}")
        except Exception as e:
            print(f"\n[ERROR] {e}")


if __name__ == "__main__":
    main()
