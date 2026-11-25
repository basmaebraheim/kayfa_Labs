
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-120b"



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

Response length:
- Keep answers short: around 3-6 sentences or a few bullet points.
- Go deeper only if the user asks for more detail.

Keep responses clear, practical, and engaging.
"""

print("Welcome to your Agentic AI Learning Coach!")
print("Let's learn and build intelligent agents together!")
print("Type 'exit' or 'quit' to end the conversation.\n")

# Groq has no chat session object, so we keep the conversation history ourselves
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

message_count = 0

while True:
    try:
        user_input = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAgent: Goodbye! Keep learning and building AI agents!")
        break

    if user_input.lower() in ["exit", "quit"]:
        print("\nAgent: Goodbye! Keep learning and building AI agents!")
        break

    if not user_input:
        continue

    message_count += 1

    print(f"\nMessage number: {message_count}")
 
    try:
         
        stream = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=True,
        )
        print(f"\nAgent: ")

        for chunk in stream:
            piece = chunk.choices[0].delta.content
            if piece:
                print(piece, end="|")
    
        messages.append({"role": "user", "content": user_input})
    
        print(f"\n")

    except Exception as e:
        # Drop the unanswered message so the history stays consistent
        messages.pop()
        print("\nAgent: Sorry, I'm temporarily unable to respond.")
        print(f"Technical details: {e}\n")
