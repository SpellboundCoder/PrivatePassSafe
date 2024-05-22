from flet import *
from controls import UserSearchBar, UserListTile
from core import AppStyle


class HomePage(Container):
    def __init__(self, home_page: Page, session):
        super().__init__(**AppStyle['window'])
        self._session = session
        self.page = home_page
        self.gradient = LinearGradient(**AppStyle['gradient'])
        self.searchBar = UserSearchBar(lambda e: self.filter_tiles(e))
        self.listTiles = UserListTile()
        self.chips = [

            Chip(
                **AppStyle['chip'],
                label=Text('All'),
                on_select=self.chip_selected,
                leading=Icon(icons.ALL_INBOX),
                selected=True,
            ),
            Chip(
                **AppStyle['chip'],
                label=Text("Favourites"),
                leading=Icon(icons.FAVORITE_BORDER_OUTLINED),
                on_select=self.chip_selected,
            ),
            Chip(
                **AppStyle['chip'],
                label=Text('Social Media'),
                leading=Icon(icons.SOCIAL_DISTANCE),
                on_select=self.chip_selected,
            ),
            Chip(
                **AppStyle['chip'],
                label=Text('Work'),
                leading=Icon(icons.WORK),
                on_select=self.chip_selected,
            ),
            Chip(
                **AppStyle['chip'],
                label=Text('test'),
                leading=Icon(icons.SOCIAL_DISTANCE),
                on_select=self.chip_selected,
            )
        ]

        self.content = Column(
            controls=[
                Text(value='PrivatePassSafe', color=colors.WHITE, size=25, weight=FontWeight.BOLD),
                Container(
                    content=self.searchBar,
                    padding=padding.only(10, right=10),
                    ),
                Container(
                    content=Row(controls=self.chips,
                                scroll=ScrollMode.HIDDEN,
                                spacing=15),
                    padding=padding.only(left=10, right=10, top=10)),

                self.listTiles,

                ],
        )

    def chip_selected(self, e):
        if e.control.label.value == 'All':
            for _chip in self.chips:
                if _chip.label.value != 'All':
                    _chip.selected = False
        else:
            self.chips[0].selected = False
        self.page.update()

    def filter_tiles(self, e):
        if e.data:
            for tile in self.listTiles.tiles:
                tile.visible = (
                    True
                    if e.data in tile.title.value
                    else False
                )
                self.listTiles.update()
        else:
            for tile in self.listTiles.tiles:
                tile.visible = True
                self.listTiles.update()
