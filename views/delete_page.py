from flet import *


class Delete(Container):
    def __init__(self, delete_page: Page):
        super().__init__()
        self.page = delete_page
        self.expand = True
        self.content = Text('Delete Page', color='red')

    def build(self):
        return NotImplementedError

