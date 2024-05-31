from flet import (BottomAppBar,
                  IconButton,
                  Row,
                  MainAxisAlignment,
                  Offset,
                  VerticalDivider,
                  Page,
                  colors,
                  )
from core import AppStyle


class UserBottomAppBar(BottomAppBar):
    def __init__(self, route: str, theme_mode: Page.theme_mode):
        super().__init__(**AppStyle(theme_mode).bottom_appbar())
        self._route = route
        self.AppStyle = AppStyle(theme_mode=theme_mode)
        self.home = IconButton(
            **self.AppStyle.home_icon(False if self._route != '/home' else True))

        self.settings = IconButton(
            **self.AppStyle.settings_icon(False if self._route != '/settings' else True))

        self.delete = IconButton(
            **self.AppStyle.delete_icon(False if self._route != '/delete' else True))

        self.update = IconButton(
            **self.AppStyle.update_icon(False if self._route != '/update' else True))

        self.content = Row([
            self.home,
            self.update,
            VerticalDivider(width=50, color=colors.TRANSPARENT),
            self.delete,
            self.settings,
        ], alignment=MainAxisAlignment.SPACE_BETWEEN,
           offset=Offset(0, -0.2))

        self.home.on_click = lambda e: self._select_home()
        self.settings.on_click = lambda e: self._select_settings()
        self.delete.on_click = lambda e: self._select_del()
        self.update.on_click = lambda e: self._select_update()

    def _select_home(self):
        self._select_icon(self.home)

    def _select_settings(self):
        self._select_icon(self.settings)

    def _select_del(self):
        self._select_icon(self.delete)

    def _select_update(self):
        self._select_icon(self.update)

    def _select_icon(self, selected_icon):
        selected_icon.selected = True

        if selected_icon == self.delete:
            if self.page.route != '/delete':
                self.page.go('/delete')

        elif selected_icon == self.home:
            if self.page.route != '/home':
                self.page.go('/home')

        elif selected_icon == self.update:
            if self.page.route != '/update':
                self.page.go('/update')

        elif selected_icon == self.settings:
            if self.page.route != '/settings':
                self.page.go('/settings')
