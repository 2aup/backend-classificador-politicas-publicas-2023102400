import os

from pydantic_settings import BaseSettings, SettingsConfigDict

# Modelo usado em todas as chamadas à Groq (personas e xai-summary).
# Fonte única: trocar de modelo é mudar esse valor, não os serviços.
DEFAULT_GROQ_MODEL = "openai/gpt-oss-20b"


def groq_model() -> str:
    """Modelo das chamadas à Groq. Sobrescrevível por GROQ_MODEL, mas a env
    var é opcional -- o default já é o modelo em uso."""
    return os.getenv("GROQ_MODEL") or DEFAULT_GROQ_MODEL


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    EMAIL_FROM: str
    DEBUG_EMAILS: bool = False
    GROQ_API_KEY: str
    ALLOWED_EMAIL_DOMAINS: str
    FILES_PATH: str
    DOCUMENTS_BASE_DIR: str | None = None
    FRONTEND_URL: str
    BACKEND_URL: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def documents_base_dir(self) -> str:
        return self.DOCUMENTS_BASE_DIR or self.FILES_PATH

settings = Settings()