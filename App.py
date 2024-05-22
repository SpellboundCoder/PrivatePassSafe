from flet import (Page,
                  View,
                  ThemeMode,
                  CrossAxisAlignment,
                  MainAxisAlignment,
                  Theme,
                  ScrollbarTheme,
                  FloatingActionButton,
                  FloatingActionButtonLocation,
                  AppBar,
                  padding,
                  app)
from controls import UserBottomAppBar
from core import AppStyle
from views import Login, HomePage, Register, Add, Delete, Settings
from data.dbconfig import engine
from sqlalchemy.orm import sessionmaker

WINDOW_HEIGHT = 740
WINDOW_WIDTH = 420
# create_database()
Session = sessionmaker(bind=engine)
session = Session()


class Main:
    def __init__(self, main_page: Page):
        super().__init__()
        self.page = main_page
        self.page.adaptive = True
        self.page.title = "Yevhen's Password-Manager"
        self.page.window_width = WINDOW_WIDTH
        self.page.window_height = WINDOW_HEIGHT
        self.page.theme_mode = ThemeMode.DARK
        self.page.window_resizable = True
        self.page.padding = padding.all(0)
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.vertical_alignment = MainAxisAlignment.CENTER
        self.page.theme = Theme(
            scrollbar_theme=ScrollbarTheme(thickness=0)
            )
        self.helper()

    def helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/home')

    def add_btn(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/add')

    def on_route_change(self, route):
        route_page = {
            '/login': Login,
            '/register': Register,
            '/home': HomePage,
            '/add': Add,
            '/delete': Delete,
            '/settings': Settings           # f'{self.page.session.get('logged_in')}/dashboard': Dashboard,
        }[self.page.route](self.page, session)
        self.page.views.clear()

        if self.page.route == '/login' or self.page.route == '/register':
            self.page.views.append(
                View(
                    route=route,
                    controls=[route_page],
                    padding=0
                )
            )
            self.page.update()
        elif self.page.route == '/add':
            self.page.views.append(
                View(
                    route=route,
                    controls=[route_page],
                    # bottom_appbar=UserBottomAppBar(route),
                    padding=0,
                    appbar=AppBar(
                        toolbar_height=10,
                        bgcolor='black'
                    )
                )
            )
            self.page.update()
        else:
            self.page.views.append(
                View(
                    route=route,
                    controls=[route_page],
                    bottom_appbar=UserBottomAppBar(self.page.route),
                    padding=0,
                    appbar=AppBar(
                        toolbar_height=10,
                        bgcolor='black'
                    ),
                    floating_action_button=FloatingActionButton(**AppStyle['floating_button'],
                                                                on_click=lambda e: self.add_btn()),
                                                                # on_click=self.page.go('/add')),
                    floating_action_button_location=FloatingActionButtonLocation.CENTER_DOCKED,
                ))
            self.page.update()


if __name__ == '__main__':
    app(target=Main, assets_dir='assets')  # , view=AppView.WEB_BROWSER, port=5050
