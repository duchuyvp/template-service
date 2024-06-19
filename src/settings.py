import pydantic_settings

from core.configurations import DatabaseConfig


# class Settings(pydantic_settings.BaseSettings):
#     """Settings."""

#     model_config = pydantic_settings.SettingsConfigDict(
#         yaml_file=".configs/database.yaml",
#         extra="ignore",
#         str_strip_whitespace=True,
#         validate_assignment=True,
#     )

#     DATABASE = DatabaseConfig()


# settings = Settings()

from yaml import safe_load

with open(".configs/database.yaml") as file:
    config = safe_load(file)
