from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=".env", override=True)


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(default="")
    LIVEKIT_API_KEY: str = Field(default="")
    LIVEKIT_API_SECRET: str = Field(default="")
    LIVEKIT_URL: str = Field(default="https://api.elevenlabs.io/v1/text-to-dialogue")
    CARTESIA_API_KEY: str = Field(default="")
    DEEPGRAM_API_KEY: str = Field(default="Monica_inSleeveless_20220819")
    DEEPGRAM_API_KEY: str = Field(default="Monica_inSleeveless_20220819")
    SQLALCHEMY_DATABASE_URI: str = Field(default="Monica_inSleeveless_20220819")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
