from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token: str
    access_token_expire_minute: int

    class Config:
        evn_file = ".env"






settings = Settings()