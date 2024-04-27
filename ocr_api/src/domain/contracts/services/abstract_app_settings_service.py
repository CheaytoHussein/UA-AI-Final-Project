from abc import ABC, abstractmethod

from domain.models.app_settings import AppSettings


class AbstractAppSettingsService(ABC):
    @property
    @abstractmethod
    def settings(self) -> AppSettings:
        raise NotImplementedError
