"""
Test script to see state access directly.
Run with: python test_state.py
"""
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
import asyncio
from dotenv import load_dotenv
load_dotenv()  # loads your existing .env file
from agent import root_agent

async def main():
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="name_extractor_app",
        user_id="test_user",
        session_id="test_session"
        )
    runner = Runner(
        agent=root_agent,
        app_name="name_extractor_app",
        session_service=session_service
        )
    user_message = Content(parts=[Part(text="Hi, my name is Alex Johnson")])
    print("=== Running agent ===")
    async for event in runner.run_async(          # ← run_async instead of run
        user_id="test_user",
        session_id="test_session",
        new_message=user_message
    ):
        if event.is_final_response():
            print(f"\nAgent response: {event.content.parts[0].text}")
    print(f"\n=== State after execution ===")
    print(f"Full state: {session.state}")
    print(f"Extracted name: {session.state.get('user_name')}")
    if session.state.get("user_name"):
        print("Name was successfully extracted and stored!")
    else:
        print("Name extraction failed")
    print("\n=== Simulating second turn ===")
    async for event in runner.run_async(          # ← run_async instead of run
        user_id="test_user",
        session_id="test_session",
        new_message=Content(parts=[Part(text="What's my name?")])
    ):
        if event.is_final_response():
            print(f"Agent response: {event.content.parts[0].text}")
            print(f"\nState still contains: {session.state.get('user_name')}")
            print("State persists across turns!")

asyncio.run(main())