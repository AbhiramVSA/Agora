from __future__ import annotations

from pydantic import BaseModel

class AgentBase(BaseModel):
    prompt: str
    
class Agent(BaseModel):
    agent: AgentBase
    