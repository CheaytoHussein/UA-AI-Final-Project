from domain.contracts.services.abstract_app_settings_service import AbstractAppSettingsService
from domain.models.app_settings import AppSettings, EnvSettings


class AppSettingsService(AbstractAppSettingsService):
    def __init__(self):
        self._settings = AppSettings.get_settings(EnvSettings())

    @property
    def settings(self) -> AppSettings:
        return self._settings
