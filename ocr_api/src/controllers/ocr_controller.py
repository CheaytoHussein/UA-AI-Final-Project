from typing import Union, List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, UploadFile

from containers import Services
from domain.contracts.services.abstract_ocr_service import AbstractOCRService
from domain.models.languages import LanguagesEnum
from domain.models.ocr_results import OCRResults

router = APIRouter()


@router.post("/singular_extraction")
@inject
async def translate_text_from_single_image(
        language: LanguagesEnum,
        save_annotated_image: bool,
        image: UploadFile,
        ocr_service: AbstractOCRService = Depends(Provide[Services.ocr_service])
) -> Union[List[OCRResults], str]:
    return await ocr_service.extract_from_image(language.value, image, save_annotated_image)
