from typing import List

from pydantic import BaseModel


class OCRResults(BaseModel):
    text: str
    text_confidence: float
    translation: str
    language: str
    box_coordinates: List[List[int]]
