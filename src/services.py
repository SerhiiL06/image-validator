import re

from fastapi import HTTPException, status
from openai import OpenAI


from core.settings import OPEN_AI_KEY

from .exceptions import SomethingWentWrong
from .utils import promt_message, urls_regex


class OpenAITools:
    __AI_KEY = OPEN_AI_KEY

    def __init__(self) -> None:
        self.client = OpenAI(api_key=self.key)

    def send_images_urls_to_validate(self, image_list: list[str]):
        correct_urls = self.__validate_urls(image_list)

        if correct_urls is None:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                {"message": "not any valid urls or image format"},
            )

        response = self._validate_images_by_urls(image_list)
        return response

    def _validate_images_by_urls(self, urls: list[str]) -> dict:

        try:
            result = []

            for u in urls:
                jpt_anwser = self.generate_anwser_message(u)

                if jpt_anwser == "0":
                    result.append(u)

            return result

        except Exception as e:
            raise SomethingWentWrong(e)

    def generate_anwser_message(self, image_url: str) -> str:
        answer = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": promt_message},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                                "detail": "low",
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        return answer.choices[0].message.content

    @classmethod
    def __validate_urls(cls, urls: list[str]) -> list[str] | None:
        accepted = []
        for u in urls:
            if re.fullmatch(urls_regex, u):
                accepted.append(u)

        return accepted if accepted else None

    @property
    def key(self) -> str:
        return self.__AI_KEY
