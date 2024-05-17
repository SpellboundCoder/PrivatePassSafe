from flet import Container


class Register(Container):
    def __init__(self):
        super().__init__()

    def build(self):
        return NotImplementedError
