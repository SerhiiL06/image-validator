class SomethingWentWrong(Exception):
    pass


class BadRequest(Exception):

    def __init__(self, code: int, *args) -> None:
        super().__init__(*args)
        self.code = code
