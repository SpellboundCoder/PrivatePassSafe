from flet import *

from core import *


class Add(Container):
    def __init__(self, add_page: Page):
        super().__init__(**window_style)
        self.page = add_page
        self.gradient = LinearGradient(**gradient)
        self.container = Container(
                width=350,
                height=600,
                bgcolor='green',
                content=Text('This is ADD page')
            )
        self.content = self.container
        # self.content = Card(
        #     width=350,
        #     height=600,
        #     expand=False,
        #     content=Text('This is ADD page')
        # )





