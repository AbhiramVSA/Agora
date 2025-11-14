import os
import asyncio
import re
from sqlalchemy import text
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from core.config import Settings

load_dotenv()

async def async_main() -> None:
    engine = create_async_engine(Settings.SQLALCHEMY_DATABASE_URI, echo=True)
    async with engine.connect() as conn:
        result = await conn.execute(text("select 'hello world'"))
        print(result.fetchall())
    await engine.dispose()

asyncio.run(async_main())