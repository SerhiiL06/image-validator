import re

from openai import OpenAI

from core.settings import OPEN_AI_KEY

from .exceptions import BadRequest, SomethingWentWrong
from .utils import prompt_message, urls_regex


class OpenAITools:
    def __init__(self) -> None:
        self._client = OpenAI(api_key=self._key)

    def send_image_urls_for_validation(
        self,
        image_list: list[str],
        detail: str = "auto",
    ) -> list:
        correct_urls = self.__validate_urls(image_list)

        if correct_urls is None:
            raise BadRequest(400)

        response = self.validate_image_by_urls(image_list, detail)
        return {"images_list": response}

    def validate_image_by_urls(
        self,
        urls: list[str],
        detail: str = "auto",
    ) -> dict:

        result = []

        for u in urls:
            gpt_answer = self.__generate_answer_message(u, self._client, detail)

            if gpt_answer == "0":
                result.append(u)

        return result

    @classmethod
    def __generate_answer_message(
        cls,
        image_url: str,
        client: OpenAI,
        detail: str = "auto",
    ) -> str:
        try:
            answer = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "assistant",
                        "content": [
                            {"type": "text", "text": prompt_message},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": image_url,
                                    "detail": detail,
                                },
                            },
                        ],
                    }
                ],
                max_tokens=300,
            )
            return answer.choices[0].message.content
        except Exception as e:
            return SomethingWentWrong(e)

    @classmethod
    def __validate_urls(cls, urls: list[str]) -> list[str] | None:
        accepted = []
        for u in urls:
            if re.fullmatch(urls_regex, u):
                accepted.append(u)

        return accepted if accepted else None

    @property
    def _key(self) -> str:
        "Return the token key from OpenAI."
        return OPEN_AI_KEY
