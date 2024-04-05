from dataclasses import dataclass
from typing import Literal


@dataclass
class ImagesListDto:
    images_list: list[str]
    detail: Literal["low", "auto", "high"] = None
