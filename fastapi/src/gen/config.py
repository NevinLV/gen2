from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    cors_allowed_origins: list[str] = []

settings = _Settings.model_validate({})
