import flet
from flet import *

width = 420*1.6
height = 405*1.6


class MenuButton(Stack):
    def __init__(self, button_icon: icons, name: str, _width: int, hover_color: str):
        super().__init__()
        self.icon = button_icon
        self.text = name
        self.hover_color = hover_color
        self.button = Container(
            Row([
                Icon(
                    self.icon,
                    color=colors.WHITE,
                    size=16
                ),
                Text(
                    self.text,
                    color=colors.WHITE,
                    size=16,
                    weight=FontWeight.W_600
                )
            ]),
            width=_width,
            bgcolor=self.hover_color,
            padding=padding.only(15, 10, 0, 10),
            border_radius=6,
            # on_hover=self.hover,
            # animate=Animation(400)
        )

    # def hover(self, e):
    #     if self.button.bgcolor != self.hover_color:
    #         self.button.bgcolor = self.hover_color
    #         self.button.blur = Blur(12, 12, BlurTileMode.MIRROR),
    #     else:
    #         self.button.bgcolor = colors.TRANSPARENT
    #         self.button.blur = None
    #     self.button.update()

    def build(self):
        return self.button


class Sidebar(Stack):
    def __init__(self):
        super().__init__()
        self.bgcolor = '#44000000'
        self.menubar = GestureDetector(
            Container(
                Row([
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor=colors.RED
                    ),
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor=colors.YELLOW
                    ),
                    Container(
                        width=10,
                        height=10,
                        border_radius=360,
                        bgcolor=colors.GREEN,
                        blur=Blur(12, 12, BlurTileMode.MIRROR),
                    )
                ]),
                height=40,
                width=240,
                bgcolor=self.bgcolor,
                padding=padding.only(20, 10, 0, 10)
            ),
            on_pan_update=self.update_pos,
        )

        self.body = Container(
            Column([
                self.menubar,
                Container(
                    Text(
                        "Menu",
                        color='#999999',
                        size=14,
                        weight=FontWeight.W_500
                    ),
                    padding=padding.only(20),
                ),
                Container(
                    Column([
                        MenuButton(icons.DASHBOARD, 'Dashboard', 240, self.bgcolor),
                        MenuButton(icons.DASHBOARD_OUTLINED, 'Message', 240, self.bgcolor),
                        MenuButton(icons.DASHBOARD, 'Users', 240, self.bgcolor),
                        MenuButton(icons.DASHBOARD, 'Rewards', 240, self.bgcolor),
                        MenuButton(icons.DELETE, 'Delete', 240, self.bgcolor),
                        MenuButton(icons.SETTINGS, 'Settings', 240, self.bgcolor),

                    ]),
                    padding=padding.only(20),
                ),
                Container(
                    Row([
                        Icon(
                            icons.LIGHT_MODE,
                            color=colors.WHITE,
                        ),
                        Switch(
                            value=True,
                            active_color=colors.BLACK87,
                            on_change=self.mode_change,
                        ),
                        Icon(
                            icons.DARK_MODE,
                            color=colors.BLACK87,
                        ),
                    ]),
                    padding=padding.only(20, 40),
                )

            ]),
            width=240,
            height=500,
            left=40,
            top=50,
            border_radius=6,
            bgcolor=self.bgcolor,
            blur=Blur(12, 12, BlurTileMode.MIRROR),
        )

    def mode_change(self, e):
        if e.control.value:
            self.bgcolor = '#44000000'
        else:
            self.bgcolor = '#11000000'
        self.body.bgcolor = self.bgcolor
        self.body.update()

    def update_pos(self, e):
        self.body.top = max(0, self.body.top+e.delta_y)
        self.body.left = max(0, self.body.left + e.delta_x)
        self.body.update()

    def build(self):
        return self.body


body = Container(
    Stack([
        Image(
            src="../../../Desktop/PrivitePassSafe/assets/gradient-bg.jpg",
            width=width,
            left=0,
            top=0
        ),
        Sidebar()
    ]),
    width=width,
    height=height
)


def manage(page: Page):
    page.window_max_width = width
    page.window_max_height = height
    page.window_width = width
    page.window_height = height
    page.window_resizable = True
    page.padding = 0

    page.add(body)
    page.update()


flet.app(manage)
