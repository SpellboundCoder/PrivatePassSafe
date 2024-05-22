from flet import (BottomAppBar,
                  IconButton,
                  Row,
                  MainAxisAlignment,
                  Offset,
                  VerticalDivider,
                  colors,
                  icons)
from core import AppStyle


class UserBottomAppBar(BottomAppBar):
    def __init__(self, route: str, *args):
        super().__init__(*args, **AppStyle['appbar'])
        self._route = route
        self.home = IconButton(icon=icons.HOME, icon_size=35, selected=False,
                               icon_color=colors.GREY if self._route != '/home' else colors.DEEP_PURPLE_ACCENT_700
                               )
        self.settings = IconButton(icon=icons.SETTINGS, icon_size=30, selected=False,
                                   icon_color=colors.GREY if self._route != '/settings'
                                   else colors.DEEP_PURPLE_ACCENT_700
                                   )
        self.delete = IconButton(icon=icons.DELETE, icon_size=30, selected=False,
                                 icon_color=colors.GREY if self._route != '/delete' else colors.RED_ACCENT_700
                                 )
        self.themeIcon = IconButton(icon=icons.LIGHT_MODE, icon_size=30, selected=False, icon_color=colors.GREY,
                                    )
        self.content = Row([
            self.home,
            self.delete,
            VerticalDivider(width=50, color=colors.TRANSPARENT),
            self.settings,
            self.themeIcon,
        ], alignment=MainAxisAlignment.SPACE_BETWEEN,
           offset=Offset(0, -0.2))

        self.home.on_click = self._select_home
        self.themeIcon.on_click = self._select_theme
        self.settings.on_click = self._select_settings
        self.delete.on_click = self._select_del

    def _select_home(self, e):
        self._select_icon(self.home)

    def _select_theme(self, e):
        self._select_icon(self.themeIcon)

    def _select_settings(self, e):
        self._select_icon(self.settings)

    def _select_del(self, e):
        self._select_icon(self.delete)

    def _select_icon(self, selected_icon):
        selected_icon.selected = True

        if selected_icon == self.delete:
            if self.page.route != '/delete':
                self.page.go('/delete')

        elif selected_icon == self.home:
            if self.page.route != '/home':
                self.page.go('/home')

        elif selected_icon == self.settings:
            if self.page.route != '/settings':
                self.page.go('/settings')

