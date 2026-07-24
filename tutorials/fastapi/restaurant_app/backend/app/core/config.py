from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Restaurant App"
    DATABASE_URL: str = "sqlite+aiosqlite:///./restaurant.db"
    CORS_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
