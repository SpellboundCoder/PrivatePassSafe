from flet import (BottomAppBar,
                  IconButton,
                  Row,
                  MainAxisAlignment,
                  colors,
                  icons)

from core import *


class UserBottomAppBar(BottomAppBar):
    def __init__(self, *args):
        super().__init__(*args, **appbar_style)

        self.homeIcon = IconButton(icon=icons.HOME, icon_size=35, selected=True,
                                   icon_color=colors.GREY)
        self.themeIcon = IconButton(icon=icons.LIGHT_MODE, icon_size=30, selected=False, icon_color=colors.GREY,
                                    offset=Offset(-0.3, 0))
        self.favIcon = IconButton(icon=icons.FAVORITE, icon_size=30, selected=False, icon_color=colors.GREY,
                                  offset=Offset(+0.3, 0))
        self.delIcon = IconButton(icon=icons.DELETE, icon_size=30, selected=False, icon_color=colors.GREY,
                                  )

        self.content = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                self.homeIcon, self.themeIcon, self.favIcon, self.delIcon
            ]
        )

        self.homeIcon.on_click = self._select_home
        self.themeIcon.on_click = self._select_search
        self.favIcon.on_click = self._select_fav
        self.delIcon.on_click = self._select_del

    def check_icon(self):
        if self.page.route == '/home':
            self.homeIcon.icon_color = colors.DEEP_PURPLE_ACCENT_700
            self.homeIcon.update()
        elif self.page.route == '/add':
            self.favIcon.icon_color = colors.DEEP_PURPLE_ACCENT_700
            self.favIcon.update()
        elif self.page.route == '/delete':
            self.delIcon.icon_color = colors.RED_ACCENT_700
            self.delIcon.update()

    def _select_home(self, e):
        self._select_icon(self.homeIcon)

    def _select_search(self, e):
        self._select_icon(self.themeIcon)

    def _select_fav(self, e):
        self._select_icon(self.favIcon)

    def _select_del(self, e):
        self._select_icon(self.delIcon)

    def _select_icon(self, selected_icon):
        # Deselect all icons
        for icon in self.content.controls:
            icon.selected = False
            icon.icon_color = colors.GREY
            icon.update()

        # Select and color the chosen icon
        selected_icon.selected = True

        if selected_icon == self.delIcon:
            self.page.go('/delete')
            self.check_icon()
            selected_icon.icon_color = colors.RED_ACCENT_700
            selected_icon.update()

        elif selected_icon == self.homeIcon:
            if self.page.route != '/home':
                self.page.go('/home')   # Update the selected icon button
            selected_icon.icon_color = colors.DEEP_PURPLE_ACCENT_700
            selected_icon.update()

        elif selected_icon == self.favIcon:
            self.page.go('/add')
            self.check_icon()
            selected_icon.icon_color = colors.DEEP_PURPLE_ACCENT_700
            selected_icon.update()
