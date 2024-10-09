from typing import Literal, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек

    Атрибуты
    --------
    DB_HOST: str
        адрес хоста сервера
    DB_PORT: int
        порт
    DB_USER: str
        имя пользователя
    DB_PASS: str
        пароль пользователя
    DB_NAME: str
        имя базы данных
    MODE: Literal["DEV", "TEST", "PROD"]  # default DEV, test activating for start tests
        режим запуска
    LOG_LEVEL: str
        режим логгирования
    """

    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    URL: str

    class Config:
        env_file = ".env"
        from_attributes = True


settings = Settings()
