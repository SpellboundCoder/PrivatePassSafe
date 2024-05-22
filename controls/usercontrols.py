import random
from typing import List
from core import *


class UserListTile(Card):
    def __init__(self):
        super().__init__(**AppStyle['listTilesCard'])
        self.elevation = 8.0
        self.margin = margin.all(10)
        self.shadow_color = colors.WHITE
        self.icon_names = dir(icons)
        self.trailing_icon = random.choice(list(self.icon_names))
        self.cont = Container(image_src='../assets/insta.jpg', width=40, height=40)
        self.content = Container(
            padding=20,
            content=Column(
                **AppStyle['columnTiles'],
                scroll=ScrollMode.HIDDEN,
                controls=[
                    ListTile(
                        **AppStyle['listTiles'],
                        style=ListTileStyle.DRAWER,
                        leading=self.cont,
                        trailing=Icon(self.trailing_icon),
                        title=Text(f"Tile{_}"),
                        on_click=self.tile_clicked,  # Add on_click event handler
                        )
                    for _ in range(15)
                ],
            ),
            )

    def tile_clicked(self, e: ControlEvent):
        print(f"Tile clicked: {e.control.title}")
        self.update()