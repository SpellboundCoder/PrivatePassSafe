import random
from typing import List
from core import *


class UserListTile(Card):
    def __init__(self: Card):
        super().__init__(**AppStyle['listTilesCard'])
        self.tiles: List[ListTile] = []
        self.elevation = 8.0
        self.margin = margin.all(10)
        self.shadow_color = colors.WHITE
        # self.img = Image(
        #     src="../assets/FB.png",
        #     width=40,
        #     height=40,
        #     fit=ImageFit.CONTAIN, )
        self.cont = Container(image_src='../assets/insta.jpg', width=40, height=40)
        self.content = Container(
            Column(
                **AppStyle['columnTiles'],
                scroll=ScrollMode.HIDDEN,
                controls=self.add_tiles(),
            ),
            padding=20)

    def tile_clicked(self, e: ControlEvent):
        print(f"Tile clicked: {e.control.title}")
        self.update()

    def add_tiles(self) -> list:
        icon_names = dir(icons)
        contain = self.cont
        for _ in range(15):
            leading_icon: str = random.choice(list(icon_names))
            trailing_icon: str = random.choice(list(icon_names))
            tile: ListTile = ListTile(
                **AppStyle['listTiles'],
                style=ListTileStyle.DRAWER,
                leading=contain,
                trailing=Icon(trailing_icon),
                title=Text(f"Tile{_}"),
                on_click=self.tile_clicked,  # Add on_click event handler

            )
            self.tiles.append(tile)
        return self.tiles
