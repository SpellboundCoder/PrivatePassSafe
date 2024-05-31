from math import pi
from flet import (Page,
                  Container,
                  LinearGradient,
                  Row,
                  Column,
                  ElevatedButton,
                  SnackBar,
                  Text,
                  FontWeight,
                  alignment,
                  MainAxisAlignment,
                  TextField,
                  TextSpan,
                  TextStyle,
                  TextDecoration,
                  Offset,
Stack,
CrossAxisAlignment,
                  icons,
                  colors,
                  ScrollMode,
                  padding)
from werkzeug.security import check_password_hash
from controls import AnimatedLock
from core import dict_en, AppStyle
from data.dbconfig import User
from time import sleep

dictionary = dict_en['Login']


class Password(Container):

    def __init__(self, pass_page: Page, session):
        super().__init__(expand=True, padding=15)
        self.page = pass_page
        self.session = session
        self.activated_lock = False

        self.AppStyle = AppStyle(self.page.theme_mode)
        self.lock = AnimatedLock(rotate_angle=pi / 4)
        self.gradient = LinearGradient(**self.AppStyle.gradient())

        self.password = TextField(
            **self.AppStyle.input_textfield(),
            label=dictionary['password'],
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock()
        )
        self.login_button = ElevatedButton(
            **self.AppStyle.primary_button(),
            text='Log In',
            on_click=lambda e: self.login_auth(),
        )
        self.password_error = SnackBar(
            Text('Wrong password!',
                 color=colors.WHITE),
            bgcolor=colors.RED
        )

        # PAGE CONTENT
        self.content = Container(
            content=Column(
                controls=[
                    Stack([
                        Container(
                            content=self.lock,
                            alignment=alignment.center,
                        ),
                        Text(**self.AppStyle.logo(), left=0, top=-5)
                    ]),
                    Container(
                        content=Column(
                            scroll=ScrollMode.HIDDEN,
                            spacing=20,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(
                                            value=f'Welcome back {self.page.client_storage.get('username')}',
                                            size=24,
                                            weight=FontWeight.BOLD)]
                                ),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(
                                            value='Please enter your password',
                                            size=20,
                                            weight=FontWeight.BOLD)],
                                    offset=Offset(0, -0.3)
                                ),
                                Row(
                                    controls=[self.password]
                                ),
                                Row(
                                    height=20,
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        Text('Forget password?',
                                             offset=Offset(0, -0.4))
                                    ]),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[self.login_button]
                                ),
                                Row(height=40),
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text("If you want to go to Login Page press ",
                                             spans=[
                                                 TextSpan(
                                                     text='here.',
                                                     on_click=lambda s: self.to_login(),
                                                     style=TextStyle(
                                                         italic=True,
                                                         decoration=TextDecoration.UNDERLINE)
                                                 )
                                             ]
                                             )
                                    ],
                                )
                            ],
                        ),
                        padding=padding.only(left=15, right=15)
                    ),
                    self.password_error,
                ]
            )
        )

    def login_auth(self):
        password = self.password.value
        email = self.page.client_storage.get(key="email")
        user = self.session.query(User).filter_by(email=email).one_or_none()
        if check_password_hash(user.password, password):
            self.lock.stop_animation()
            self.page.session.set(key="username", value=user.username)
            self.page.session.set(key="email", value=user.email)
            sleep(0.5)
            self.page.go('/home')
        else:
            self.password_error.open = True
            self.password_error.update()

    def activate_lock(self):
        if not self.activated_lock:
            self.activated_lock = True
            self.lock.animate_lock()

    def to_login(self):
        self.page.go('/login')
