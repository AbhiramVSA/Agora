from livekit.agents import AgentSession, JobContext
from livekit import agents

from core.debate_agent import DebateAgent

from dotenv import load_dotenv
from app.core.config import Settings

load_dotenv()

print(Settings.OPENAI_API_KEY)

async def agent_entrypoint(ctx: JobContext):
    """Simple multi-agent entry point"""
    await ctx.connect()

    # Create session
    session = AgentSession()

    # Start with sales agent
    await session.start(
        agent=DebateAgent(),
        room=ctx.room
    )

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=agent_entrypoint))
