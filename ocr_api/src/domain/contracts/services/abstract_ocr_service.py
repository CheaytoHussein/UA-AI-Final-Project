from abc import ABC, abstractmethod
from typing import Union, List

from fastapi import UploadFile

from domain.models.ocr_results import OCRResults


class AbstractOCRService(ABC):
    @abstractmethod
    async def extract_from_image(self, language: str, image: UploadFile, save_image: bool) -> Union[List[OCRResults], str]:
        raise NotImplementedError
