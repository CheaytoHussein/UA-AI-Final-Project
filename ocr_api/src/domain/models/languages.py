from enum import Enum
from typing import Dict, List

from pydantic import BaseModel


class Language(BaseModel):
    languages_dict: Dict[str, str] = {
        'italian': 'it',
        'german': 'de',
        'french': 'fr',
        'spanish': 'es'
    }
    languages_list: List[str] = [
        'italian',
        'german',
        'french',
        'spanish'
    ]


class LanguagesEnum(Enum):
    italian: str = 'italian'
    german: str = 'german'
    french: str = 'french'
    spanish: str = 'spanish'
