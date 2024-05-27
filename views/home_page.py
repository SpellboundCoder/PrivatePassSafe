from flet import *
from controls import UserSearchBar
from core import AppStyle
from data.dbconfig import Website, User
from typing import Iterable


class HomePage(Container):
    def __init__(self, home_page: Page, session):
        super().__init__(**AppStyle['window'])
        self.page = home_page
        self.user = session.query(User).filter_by(email=self.page.session.get('email')).one_or_none()
        self.websites = self.user.websites
        self.gradient = LinearGradient(**AppStyle['gradient'])
        self.searchBar = UserSearchBar(lambda e: self.filter_tiles(e))
        self.theme = Theme()
        self.chips = Chips(lambda e: self.chip_selected(e))
        self.card = PasswordsCard(self.page.height, self.websites)
        self.content = Column(
            controls=[
                Text(value='PrivatePassSafe', color=colors.WHITE, size=25, weight=FontWeight.BOLD),
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
        if e.control.label.value == 'All':
            for _chip in self.chips.controls:
                if _chip.label.value != 'All':
                    _chip.selected = False
        else:
            self.chips.controls[0].selected = False
        self.page.update()

    def filter_tiles(self, e):
        e.control.close_view()
        if e.data:
            for tile in self.card.content.controls:
                tile.visible = (
                    True
                    if e.data in tile.content.controls[0].controls[1].value
                    else False
                )
                self.card.update()
        else:
            for tile in self.card.content.controls:
                tile.visible = True
                self.card.update()


class Chips(Row):
    def __init__(self, func):
        super().__init__()
        self.scroll = ScrollMode.HIDDEN
        self.spacing = 15
        self.tags = ['All', 'Favorite', 'Social Media', 'Entertainment', 'Messengers', 'Work', 'Study']
        self.icons = [icons.ALL_INBOX, icons.FAVORITE_BORDER, icons.FACEBOOK, icons.EMOJI_EMOTIONS, icons.MESSENGER, icons.WORK, icons.SCHOOL]
        self.controls = [
            Chip(**AppStyle['chip'],
                 label=Text(f'{self.tags[i]}'),
                 leading=Icon(self.icons[i]),
                 on_select=func,
                 selected=True if i == 0 else False)
            for i in range(len(self.tags))
        ]


class PasswordsCard(Card):
    def __init__(self, height, websites: Iterable):
        super().__init__(**AppStyle['PasswordsCard'])
        self.height = height * 0.7
        self.clip_behavior = ClipBehavior.HARD_EDGE
        self.containers = [
            Container(Stack([
                Row([
                    Image(src=website.icon, width=50),
                    Text(value=website.website, size=20, weight=FontWeight.BOLD)],
                    expand=True),
                Column([
                    Row([
                        Image(src=website.icon, width=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.website, label='Website'),
                        Container(width=45)
                    ]),
                    Row([
                        Icon(name=icons.ACCOUNT_CIRCLE, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.username, label='Username'),
                        IconButton(**AppStyle['icon_copy']),
                    ]),
                    Row([
                        Icon(name=icons.EMAIL, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.email, label='Email'),
                        IconButton(**AppStyle['icon_copy']),
                    ]),
                    Row([
                        Icon(name=icons.PASSWORD, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.password, label='Password'),
                        IconButton(**AppStyle['icon_copy'])
                    ]),
                    Row([
                        Icon(name=icons.PHONE, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.mobile, label='Mobile'),
                        IconButton(**AppStyle['icon_copy'])
                    ]),
                    Row([
                        Icon(name=icons.DATE_RANGE, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.date, label='Edited on'),
                        Container(width=45)
                    ]),
                    Row([
                        Icon(name=icons.TAG, size=30),
                        TextField(**AppStyle['read_only_textfield'], value=website.tag, label='Tag', ),
                        Container(width=45)
                    ])      # yevgenphk@gmail.com   Jonathan0758
                ], visible=False, alignment=MainAxisAlignment.START, spacing=0, scroll=ScrollMode.HIDDEN)
            ]),
                bgcolor=colors.GREY_900,
                height=50,
                shadow=BoxShadow(color=colors.GREY, blur_radius=1.1),
                animate=animation.Animation(700, AnimationCurve.EASE_IN_OUT),
                border_radius=15,
                margin=margin.only(left=15, right=15, top=10),
                on_click=lambda e: self.pop_up(e),
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
