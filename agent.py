from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    WorkerOptions,
    cli,
)
from livekit.plugins import openai, deepgram
from dotenv import load_dotenv
import os

load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=deepgram.STT(model="nova-3"),
        llm=openai.LLM(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        ),
        tts=deepgram.TTS(),
    )

    await session.start(
        room=ctx.room,
        agent=Agent(instructions="You are a friendly, concise voice assistant."),
    )

    await session.generate_reply(
        instructions="Greet the user warmly and ask how you can help them today."
    )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))