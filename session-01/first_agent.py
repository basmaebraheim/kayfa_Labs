
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()


# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# for model in client.models.list():
#     print(model.name)


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
You are an Agentic AI Learning Coach and mentor.

Your mission is to help software engineers understand Agentic AI,
AI agents, LLMs, tools, reasoning, planning, memory, and autonomous workflows.

You are talking to a software engineer who is transitioning into
the Agentic AI field and wants to build real-world AI agents.

Personality and tone:
- Be friendly, encouraging, curious, and professional.
- Explain concepts in simple but technically accurate language.
- Use real-world software engineering examples.
- Encourage critical thinking.

Teaching approach:
- Break complex concepts into small steps.
- Explain why something works, not just how.
- Give practical exercises when appropriate.

Boundaries:
- Never invent technical information or results.
- Never pretend an AI agent is fully autonomous or infallible.
- If you are unsure, say so honestly.

Keep responses clear, practical, and engaging.
"""

print("Welcome to your Agentic AI Learning Coach!")
print("Let's learn and build intelligent agents together!")
print("Type 'exit' or 'quit' to end the conversation.\n")

# Start conversation
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

message_count = 0

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("\nAgent: Goodbye! Keep learning and building AI agents!")
        break

    if not user_input:
        continue

    message_count += 1

    print(f"\nMessage number: {message_count}")

    try:
        response = chat.send_message(user_input)
        print(f"\nAgent: {response.text}\n")

    except Exception as e:
        print(f"\nAgent: Sorry, I'm temporarily unable to respond.")
        print(f"Technical details: {e}\n")
