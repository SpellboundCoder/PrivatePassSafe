import random
from typing import Union, List

from flet import (TextField,
                  ListTile,
                  Column,
                  Icon,
                  ControlEvent,
                  ScrollMode,
                  Text,
                  ListTileStyle,
                  Card
                  )

from core import *


class UserView(View):
    pass


class UserInputField(TextField):
    def __init__(self, unique_key: Union[str, None] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.unique_key = unique_key


class UserListTile(Card):
    def __init__(self: Card):
        super().__init__(**listTilesCard)
        self.tiles: List[ListTile] = []
        self.elevation = 2.0
        self.shadow_color = colors.WHITE
        self.content = Card(
            margin=margin.all(10),
            is_semantic_container=False,
            color=colors.BLACK12,
            content=Column(
                **columnTiles,
                scroll=ScrollMode.HIDDEN,
                controls=self.add_tiles(),

            )
        )

    def tile_clicked(self, e: ControlEvent):
        print(f"Tile clicked: {e.control.title}")
        self.update()

    def add_tiles(self) -> list:
        icon_names = dir(icons)
        for _ in range(15):
            leading_icon: str = random.choice(list(icon_names))
            trailing_icon: str = random.choice(list(icon_names))
            tile: ListTile = ListTile(
                **listTiles,
                style=ListTileStyle.DRAWER,
                leading=Icon(leading_icon),
                trailing=Icon(trailing_icon),
                title=Text("Tile"),
                on_click=self.tile_clicked,  # Add on_click event handler
            )
            self.tiles.append(tile)
        return self.tiles
