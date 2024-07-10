from flet import (Container,
                  Page,
                  Column,
                  LinearGradient,
                  Text,
                  padding,
                  colors,
                  icons)
from controls import UserSearchBar, PasswordsCard, Chips
from core import AppStyle
from data.dbconfig import User
from time import sleep


class HomePage(Container):
    def __init__(self, home_page: Page, session):
        super().__init__(expand=True, padding=10)
        self.page = home_page
        self.db_session = session

        self.AppStyle = AppStyle(self.page.theme_mode)
        self.user = session.query(User).filter_by(email=self.page.session.get('email')).one_or_none()
        self.websites = self.user.websites
        self.gradient = LinearGradient(**self.AppStyle.gradient())

        self.searchBar = UserSearchBar(lambda e: self.filter_tiles(e), self.page.theme_mode)

        self.chips = Chips(lambda e: self.chip_selected(e), self.page.theme_mode)

        self.card = PasswordsCard(self.page.height,
                                  self.websites,
                                  lambda e: self.favourite_selected(e),
                                  self.page.theme_mode,
                                  self.page)
        self.content = Column(
            controls=[
                Text(**self.AppStyle.logo()),
                Container(
                    content=self.searchBar,
                    padding=padding.only(10, right=10),
                    ),
                Container(
                    content=self.chips,
                    padding=padding.only(left=20, right=20, top=10)
                ),
                self.card
                ],
        )

    def chip_selected(self, e):
        for _chip in self.chips.controls:
            if _chip.label.value == e.control.label.value:
                _chip.selected = True
            else:
                _chip.selected = False

        def filter_by_tags():
            for chip_ in self.chips.controls:
                if chip_.selected:
                    for tile in self.card.content.controls:
                        tile.visible = (
                            True
                            if chip_.label.value == tile.data or chip_.label.value == 'All'
                            else False
                        )
                        self.page.update()

        filter_by_tags()
        self.page.update()

    def favourite_selected(self, e):
        website = e.control.data
        if not self.page.client_storage.contains_key(f"{website.website}"):
            self.page.client_storage.set(f"{website.website}", website.tag)
        if not e.control.selected:
            e.control.selected = True
            e.control.icon = icons.STAR
            e.control.icon_color = colors.AMBER_ACCENT_700
            website.tag = 'Favorite'
            self.db_session.commit()
            sleep(0.5)
            self.card.update()
        else:
            e.control.selected = False
            e.control.icon = icons.STAR_OUTLINE
            e.control.icon_color = colors.GREY
            website.tag = self.page.client_storage.get(f"{website.website}")
            self.db_session.commit()
            sleep(0.5)
            self.card.update()
        self.page.update()

    def filter_tiles(self, e):
        if e.data:
            for tile in self.card.content.controls:
                tile.visible = (
                    True
                    if e.data.lower() in tile.content.controls[0].controls[1].value.lower()
                    else False
                )
            self.page.update()
        else:
            for tile in self.card.content.controls:
                tile.visible = True
            self.page.update()
