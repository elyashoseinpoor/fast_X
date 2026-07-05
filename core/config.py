from pydantic_settings import BaseSettings, SettingsConfigDict

#doc : https://fastapi.tiangolo.com/advanced/settings/#read-settings-from-env

class Settings(BaseSettings):
    DATABASE_URL: str #= "sqlite:///./database.db"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()