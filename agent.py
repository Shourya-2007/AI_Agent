import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load variables from .env
load_dotenv()


def create_coding_agent():

    # Check whether API key exists
    if not os.environ.get("Gemini_API_Key"):
        print("❌ Error: Gemini_api_key is not set in the .env file.")
        return

    # Initialize Gemini client
    client = genai.Client()

    # System instruction for the AI agent
    system_instruction = (
        "You are an expert AI Software Engineer and Technical Architect assistant. "
        "Your role is to help the user write, debug, refactor, explain, "
        "and structure Python and software projects. "
        "When requested, generate complete, clean, documented, and modular code. "
        "Explain code clearly when necessary. "
        "For mathematical or algorithmic problems, use code execution when useful."
    )

    # Configure the AI agent
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,
        tools=[
            types.Tool(
                code_execution=types.ToolCodeExecution
            )
        ]
    )

    # Create persistent chat session
    chat = client.chats.create(
        model="gemini-3.5-flash",
        config=config
    )

    # Welcome message
    print("=" * 60)
    print("🤖 AI CODING & PROJECT ASSISTANT")
    print("=" * 60)
    print("Agent initialized successfully!")
    print("Type 'exit' or 'quit' to stop the agent.")
    print("=" * 60)

    # Main conversation loop
    while True:
        try:
            user_input = input("\n👤 You: ").strip()

            # Ignore empty input
            if not user_input:
                continue

            # Exit commands
            if user_input.lower() in ["exit", "quit"]:
                print("\n👋 Exiting AI Agent. Happy coding!")
                break

            print("\n🤖 Agent is thinking...\n")

            # Send user message to Gemini
            response = chat.send_message(user_input)

            # Display response
            print("🤖 Agent:")
            print(response.text)

        except KeyboardInterrupt:
            print("\n\n👋 Agent stopped by user.")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}")


# Program entry point
if __name__ == "__main__":
    create_coding_agent()