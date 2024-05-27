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
                  icons,
                  colors,
                  ScrollMode)
from werkzeug.security import check_password_hash
from controls import AnimatedLock, EmailRow
from core import AppStyle, dict_en
from data.dbconfig import User
from time import sleep

dictionary = dict_en['Login']


class Login(Container):
    def __init__(self, login_page: Page, session):
        super().__init__(**AppStyle['login/register_window'])
        self.page = login_page
        self.session = session
        self.lock = AnimatedLock(rotate_angle=pi / 4)
        self.activated_lock = False
        self.gradient = LinearGradient(**AppStyle['gradient'])

        # LOGIN Form
        self.login_email = EmailRow(lambda e: self.activate_lock())

        self.login_password = TextField(
            **AppStyle['input_textfield'],
            label=dictionary['password'],
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock()
        )
        self.login_button = ElevatedButton(
            **AppStyle['loginButton'],
            on_click=lambda e: self.login_auth(),
        )
        self.login_error = SnackBar(
            Text(dictionary['error'], color=colors.WHITE),
            **AppStyle['snack_bar']
        )

        # PAGE CONTENT
        self.content = Container(
            content=Column(
                controls=[
                    Container(
                        content=self.lock,
                        alignment=alignment.center,
                    ),
                    Container(
                        content=Column(
                            scroll=ScrollMode.HIDDEN,
                            spacing=20,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.CENTER,
                                    controls=[
                                        Text(
                                            value='Welcome to PrivatePassSafe',
                                            size=24,
                                            weight=FontWeight.BOLD)]
                                ),
                                self.login_email,
                                Row(
                                    controls=[self.login_password]
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
                                        Text("Don't have an account yet? Sign up ",
                                             spans=[
                                                 TextSpan(
                                                     text='here.',
                                                     on_click=lambda s: self.to_register(),
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
                        **AppStyle['form']
                    ),
                    self.login_error,
                ]
            )
        )

    def login_auth(self):
        email = self.login_email.controls[0].value
        password = self.login_password.value
        user = self.session.query(User).filter_by(email=email).one_or_none()
        if user:
            if check_password_hash(user.password, password):
                self.page.session.set(key="username", value=user.username)
                self.page.session.set(key="email", value=user.email)
                self.lock.stop_animation()
                sleep(0.5)
                self.page.go('/home')
            else:
                self.login_error.open = True
                self.login_error.update()
        else:
            self.login_error.open = True
            self.login_error.update()

    def activate_lock(self):
        if not self.activated_lock:
            self.activated_lock = True
            self.lock.animate_lock()

    def to_register(self):
        self.page.go('/register')
