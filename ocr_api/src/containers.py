from dependency_injector import containers, providers

from application.services.ocr_service import OCRService
from domain.contracts.services.abstract_app_settings_service import AbstractAppSettingsService
from domain.contracts.services.abstract_ocr_service import AbstractOCRService
from persistence.services.app_settings_service import AppSettingsService


class GlobalServices(containers.DeclarativeContainer):
    app_settings_service = providers.Singleton(AbstractAppSettingsService.register(AppSettingsService))


class Services(containers.DeclarativeContainer):
    ocr_service = providers.Factory(AbstractOCRService.register(OCRService), app_settings_service=GlobalServices.app_settings_service)
