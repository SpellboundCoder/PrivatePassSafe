from flet import *

from controls import UserBottomAppBar
from core import *
from views import Login, HomePage, Register, Add, Delete


# create_database()


class Main:
    def __init__(self, main_page: Page):
        super().__init__()
        self.page = main_page
        # self.page.adaptive = True
        self.page.title = "Yevhen's Password-Manager"
        self.page.window_width = WINDOW_WIDTH
        self.page.window_height = WINDOW_HEIGHT
        self.page.theme_mode = ThemeMode.DARK
        self.page.window_resizable = False
        self.page.padding = padding.all(0)
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.vertical_alignment = MainAxisAlignment.CENTER
        self.page.theme = Theme(
            scrollbar_theme=ScrollbarTheme(
                thickness=0,
            )
        )
        self.helper()

    def helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/delete')

    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        self.page.update()

    def on_route_change(self, route):
        route_page = {
            '/login': Login,
            '/home': HomePage,
            '/register': Register,
            '/add': Add,
            '/delete': Delete          # f'{self.page.session.get('logged_in')}/dashboard': Dashboard,
        }[self.page.route](self.page)
        self.page.views.clear()
        self.page.views.append(
            View(
                 route=route,
                 controls=[route_page],
                 padding=0
            )
        )
        if self.page.route == '/login' or self.page.route == '/register':
            self.page.views.append(
                View(
                    route=route,
                    controls=[route_page],
                    padding=0
                )
            )
            self.page.update()
        else:
            self.page.views.append(
                View(
                    route=route,
                    controls=[route_page],
                    bottom_appbar=UserBottomAppBar(),
                    floating_action_button=FloatingActionButton(**floating_button),
                    floating_action_button_location=(227, 60),
                    padding=0
                ))
            self.page.update()


if __name__ == '__main__':
    app(target=Main, assets_dir='/assets')  # , view=AppView.WEB_BROWSER, port=5050
