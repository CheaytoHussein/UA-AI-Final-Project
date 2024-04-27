import os.path
import uuid
from typing import List, Union

import cv2
import numpy as np
from easyocr import Reader
from fastapi import UploadFile

from application.helpers.ocr_helper import format_results, write_to_json
from domain.contracts.services.abstract_app_settings_service import AbstractAppSettingsService
from domain.contracts.services.abstract_ocr_service import AbstractOCRService
from domain.exceptions.app_exception import AppException
from domain.models.ocr_results import OCRResults


class OCRService(AbstractOCRService):

    def __init__(self, app_settings_service: AbstractAppSettingsService):
        self._app_settings = app_settings_service.settings

    async def extract_from_image(self, language: str, image: Union[UploadFile, str], save_image: bool) -> Union[List[OCRResults], str]:
        try:
            _, image_extension = os.path.splitext(image.filename)
            image = await image.read()
            image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
        except AppException as e:
            _, image_extension = os.path.splitext(image)
            image = cv2.imread(image)

        reader = Reader(['en'])

        results: List[OCRResults] = format_results(
            reader.readtext(image),
            language
        )

        ocr_uuid = str(uuid.uuid4())
        ocr_directory = os.path.join(self._app_settings.images_dir, ocr_uuid)

        os.makedirs(ocr_directory)

        json_path = os.path.join(ocr_directory, f"{ocr_uuid}.json")

        write_to_json(
            json_path,
            results
        )
        if not save_image:
            return results

        for result in results:
            image = cv2.rectangle(
                image,
                result.box_coordinates[0],  # coordinates to the top left point
                result.box_coordinates[1],  # coordinates to the bottom right point
                (255, 255, 255),
                -1  # border width (px)
            )

            image = cv2.putText(
                image,
                result.translation,
                (result.box_coordinates[0][0], result.box_coordinates[1][1] - 10),  # text placement
                cv2.FONT_HERSHEY_COMPLEX,  # font style
                0.8,  # font scale
                (0,) * 3,  # font color
                2,  # thickness in pixels
            )

        image_path = os.path.join(ocr_directory, f"{ocr_uuid}{image_extension}")

        cv2.imwrite(
            image_path,
            image
        )

        return ocr_uuid
