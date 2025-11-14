from __future__ import annotations

from pydantic import BaseModel
from agent_schema import Agent

class DebateSession(BaseModel):
    agent: Agent 
    
    
