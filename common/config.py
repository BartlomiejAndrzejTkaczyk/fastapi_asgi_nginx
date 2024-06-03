from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    celery_broker_url: str
    celery_result_backend: str

    class Config:
        env_file = "../.local_env"


settings = Settings()
