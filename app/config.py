from pydantic import BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_port: str
    database_uri: str
    database_name: str
    secret_key: str
    algorithm: str
    access_toke_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()