from flet import (Card,
                  Container,
                  Stack,
                  Column,
                  Row,
                  Image,
                  Text,
                  TextField,
                  ClipBehavior,
                  FontWeight,
                  Icon,
                  IconButton,
                  MainAxisAlignment,
                  ScrollMode,
                  Page,
                  icons,
                  colors,
                  )
from core import AppStyle
from typing import Iterable
from func import Encryption


class PasswordsCard(Card):
    def __init__(self, height: int, websites: Iterable, func, theme_mode: Page.theme_mode, page: Page):
        super().__init__(**AppStyle(theme_mode).passwords_card())
        self.height = height * 0.7
        self.page = page

        self.clip_behavior = ClipBehavior.HARD_EDGE
        self.AppStyle = AppStyle(theme_mode)
        self.Encryption = Encryption(self.page.session.get('pass'))

        self.containers = [
            Container(Stack([
                Row([
                    Image(src=website.icon, width=50),
                    Text(value=website.website, size=20, weight=FontWeight.BOLD),
                    Container(expand=True),
                    IconButton(icon=icons.STAR_OUTLINE if website.tag != 'Favorite' else icons.STAR,
                               selected=False if website.tag != 'Favorite' else True,
                               icon_color=colors.GREY if website.tag != 'Favorite' else colors.AMBER_ACCENT_700,
                               data=website,
                               on_click=lambda e: func(e))
                ], expand=True),
                Column([
                    Row([
                        Image(src=website.icon, width=30),
                        TextField(**self.AppStyle.read_only(), value=website.website, label='Website'),
                        Container(width=45)
                    ]),
                    Row([
                        Icon(name=icons.ACCOUNT_CIRCLE, size=30),
                        TextField(**self.AppStyle.read_only(),
                                  value=self.Encryption.decrypt_data(website.username) if website.username else "",
                                  label='Username'),
                        IconButton(**self.AppStyle.icon_copy()),
                    ]),
                    Row([
                        Icon(name=icons.EMAIL, size=30),
                        TextField(**self.AppStyle.read_only(),
                                  value=self.Encryption.decrypt_data(website.email),
                                  label='Email'),
                        IconButton(**self.AppStyle.icon_copy()),
                    ]),
                    Row([
                        Icon(name=icons.PASSWORD, size=30),
                        TextField(**self.AppStyle.read_only(),
                                  value=self.Encryption.decrypt_data(website.password),
                                  label='Password'),
                        IconButton(**self.AppStyle.icon_copy())
                    ]),
                    Row([
                        Icon(name=icons.PHONE, size=30),
                        TextField(**self.AppStyle.read_only(),
                                  value=self.Encryption.decrypt_data(website.mobile) if website.mobile else "",
                                  label='Mobile'),
                        IconButton(**self.AppStyle.icon_copy())
                    ]),
                    Row([
                        Icon(name=icons.DATE_RANGE, size=30),
                        TextField(**self.AppStyle.read_only(), value=website.date, label='Edited on'),
                        Container(width=45)
                    ]),
                    Row([
                        Icon(name=icons.TAG, size=30),
                        TextField(**self.AppStyle.read_only(), value=website.tag, label='Tag', ),
                        Container(width=45)
                    ])
                ], visible=False, alignment=MainAxisAlignment.START, spacing=0, scroll=ScrollMode.HIDDEN)
            ]),
                **self.AppStyle.password_tile(),
                on_click=lambda e: self.pop_up(e),
                data=website.tag
            )
            for website in websites]

        self.content = Column(
            self.containers,
            scroll=ScrollMode.HIDDEN
        )

    def pop_up(self, e):
        for _container in self.containers:
            if _container.height != 50:
                if _container is not e.control:
                    _container.height = 50
                    _container.content.controls[1].visible = False
                    _container.content.controls[0].visible = True
                    _container.update()
        if e.control.height == 50:
            e.control.height = None
            e.control.content.controls[0].visible = False
            e.control.content.controls[1].visible = True
            e.control.update()
        else:
            e.control.height = 50
            e.control.content.controls[1].visible = False
            e.control.content.controls[0].visible = True
            e.control.update()
