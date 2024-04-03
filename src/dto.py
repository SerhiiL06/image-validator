from dataclasses import dataclass


@dataclass
class ImagesListDto:
    images_list: list[str]
