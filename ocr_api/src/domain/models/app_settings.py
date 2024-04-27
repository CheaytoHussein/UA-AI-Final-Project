import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    app_dir: str


class AppSettings(BaseModel):
    app_dir: str
    datasets_dir: str
    config_dir: str
    images_dir: str

    @classmethod
    def get_settings(cls, env: EnvSettings):
        return cls(
            app_dir=env.app_dir,
            datasets_dir=os.path.join(env.app_dir, "datasets"),
            config_dir=os.path.join(env.app_dir, "config"),
            images_dir=os.path.join(env.app_dir, "images"),
        )
