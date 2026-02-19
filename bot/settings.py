from typing import Optional
from urllib.parse import quote

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Telegram auth
    TELEGRAM_API_TOKEN: str
    TELEGRAM_API_SERVER: Optional[str] = None
    TELEGRAM_API_PORT: Optional[int] = None
    BOT_ADMINS: list

    @property
    def api_server_url(self):
        if self.TELEGRAM_API_SERVER and self.TELEGRAM_API_PORT:
            return f"http://{self.TELEGRAM_API_SERVER}:{self.TELEGRAM_API_PORT}"

    # TEMP_DIR: str

    # Path to webhook route, on which Telegram will send requests
    WEBHOOK_PATH: Optional[str] = None
    # Secret key to validate requests from Telegram (optional)
    WEBHOOK_SECRET: Optional[str] = None
    WEBHOOK_PORT: Optional[int] = None
    # Base URL for webhook will be used to generate webhook URL for Telegram,
    # in this example it is used public DNS with HTTPS support
    BASE_WEBHOOK_URL: Optional[str] = None

    @property
    def webhook(self):
        if self.BASE_WEBHOOK_URL and self.WEBHOOK_PORT and self.WEBHOOK_PATH:
            return f"{self.BASE_WEBHOOK_URL}:{self.WEBHOOK_PORT}{self.WEBHOOK_PATH}"

    # Proxy
    PROXY_URL: Optional[str] = None
    PROXY_SECRET: Optional[str] = None

    # Rest api for admin app
    REST_API_ADMIN_LINK: Optional[str] = None
    REST_API_ADMIN_TOKEN: Optional[str] = None

    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    @property
    def database_url(self) -> str:
        user = f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
        database = f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return f"postgresql+asyncpg://{user}@{database}"

    # Redis
    REDIS_HOST: str
    REDIS_PORT: int

    # RabbitMQ
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str

    @property
    def rabbitmq_url(self) -> str:
        return (
            f"amqp://{self.RABBITMQ_DEFAULT_USER}:{quote(self.RABBITMQ_DEFAULT_PASS)}@" f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"
        )
    
    QUEUE_NAME: str
    EXCHANGE_NAME: str


    # Email
    # class Email:
    #     EMAIL_SERVER: str
    #     EMAIL_PORT: int
    #     SENDER_EMAIL: str
    #     EMAIL_LOGIN: str
    #     EMAIL_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")
    # class Config:
    #     env_file = ".env" if os.path.exists(".env") else None


# Объект с переменными окружения
settings = Settings()

