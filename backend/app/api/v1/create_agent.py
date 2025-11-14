from fastapi import APIRouter
from dotenv import load_dotenv
from core.debate_agent import DebateAgent
from schemas.debate_schema import DebateSession
from livekit.agents import AgentSession, JobContext

router = APIRouter()

load_dotenv()

@router.post("/start-debate-session", response_model=DebateSession)
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

