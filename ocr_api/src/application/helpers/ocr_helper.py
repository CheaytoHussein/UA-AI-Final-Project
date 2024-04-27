import json
from typing import List

from googletrans import Translator

from domain.models.languages import Language
from domain.models.ocr_results import OCRResults


def format_results(results: List, language: str) -> List:
    formatted_results: List[OCRResults] = []
    translator = Translator()

    def format_translated_text(text: str) -> str:
        text = text.replace("\u00e9", "e")
        text = text.replace("\u00E8", "e")
        text = text.replace("\u00ea", "e")
        text = text.replace("\u00C9", "E")
        text = text.replace("\u00C8", "E")
        text = text.replace("\u00CA", "E")


        text = text.replace("\u00e2", "a")
        text = text.replace("\u00E1", "a")
        text = text.replace("\u00E0", "a")
        text = text.replace("\u00C1", "A")
        text = text.replace("\u00C0", "A")
        text = text.replace("\u00C2", "A")

        text = text.replace("\u00ED", "i")
        text = text.replace("\u00EC", "i")
        text = text.replace("\u00ef", "i")
        text = text.replace("\u00ee", "i")
        text = text.replace("\u00CD", "I")
        text = text.replace("\u00CC", "I")
        text = text.replace("\u00CE", "I")
        text = text.replace("\u00CF", "I")

        text = text.replace("\u00FA", "u")
        text = text.replace("\u00F9", "u")
        text = text.replace("\u00fc", "u")
        text = text.replace("\u00fb", "u")
        text = text.replace("\u00DA", "U")
        text = text.replace("\u00D9", "U")
        text = text.replace("\u00DB", "U")
        text = text.replace("\u00DC", "U")

        text = text.replace("\u00F3", "o")
        text = text.replace("\u00F2", "o")
        text = text.replace("\u00f6", "o")
        text = text.replace("\u00f6", "o")
        text = text.replace("\u00D3", "O")
        text = text.replace("\u00D2", "O")
        text = text.replace("\u00D4", "O")
        text = text.replace("\u00D6", "O")

        return text

    for result in results:
        result = {
            # result[0] contains 4 point coordinates for a bounding box while only 2 are needed (top left, bottom right)
            "box_coordinates": [
                [int(result[0][0][0]), int(result[0][0][1])],
                [int(result[0][-2][0]), int(result[0][-2][1])]
            ],
            "text": result[1],
            "text_confidence": result[2],
            "language": language,
            "translation": format_translated_text(translator.translate(result[1], dest=Language().languages_dict[language]).text)
        }
        formatted_results.append(
            OCRResults(
                **result
            )
        )

    return formatted_results


def write_to_json(filename: str, results: List[OCRResults]):
    with open(filename, "w") as f:
        json.dump([dict(result) for result in results], f)
