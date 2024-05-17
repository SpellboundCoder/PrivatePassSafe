from flet import *

from controls import (UserSearchBar,
                      UserListTile)
from core import *


class HomePage(Container):
    def __init__(self, home_page: Page):
        super().__init__(**window_style)
        self.searchBar = UserSearchBar()
        self.listTiles = UserListTile()
        self.chips = [
            Chip(
                label=Text("Save to favourites"),
                leading=Icon(icons.FAVORITE_BORDER_OUTLINED),
                bgcolor=colors.GREEN_200,
                disabled_color=colors.BLACK,
                autofocus=False,
                on_select=self.chip_selected,
            ),
            Chip(
                label=Text('test2'),
                bgcolor=colors.GREEN_900,
                disabled_color=colors.BLACK,
                autofocus=False,
                on_select=self.chip_selected,
                show_checkmark=False,
                click_elevation=20
            )
        ]
        self.gradient = LinearGradient(**gradient)
        self.content = Stack(
            controls=[
                Container(
                    content=Row(
                        [
                         self.searchBar,
                         ],
                        alignment=MainAxisAlignment.SPACE_BETWEEN),
                    padding=padding.only(10, top=20, right=10),
                    ),
                Row(controls=self.chips, top=100, left=100),
                self.listTiles]
        )

    def show_searchbar(self):
        if self.searchBar.controls[0].opacity == 0:
            self.searchBar.controls[0].opacity = 1
            self.searchBar.controls[0].update()
        else:
            self.searchBar.controls[0].opacity = 0
            self.searchBar.controls[0].update()

    def chip_selected(self, e):
        self.page.update()
