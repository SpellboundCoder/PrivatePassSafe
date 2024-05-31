from flet import (Container,
                  LinearGradient,
                  TextField,
                  ElevatedButton,
                  SnackBar,
                  Text,
                  Row,
                  Column,
                  MainAxisAlignment,
                  Page,
                  TextSpan,
                  TextStyle,
                  TextDecoration,
                  Divider,
                  colors,
                  icons,
                  alignment,
                  padding
                  )
from controls import AnimatedLock, EmailRow
from core import dict_en, AppStyle
from math import pi
from werkzeug.security import generate_password_hash
from data.dbconfig import User
from time import sleep

dictionary = dict_en['Register']


class Register(Container):
    def __init__(self, login_page: Page, session): # noqa
        super().__init__(expand=True, padding=15)
        self.page = login_page
        self._session = session
        self.activated_lock = False

        self.AppStyle = AppStyle(self.page.theme_mode)
        self.lock = AnimatedLock(rotate_angle=pi / 4)
        self.gradient = LinearGradient(**self.AppStyle.gradient())

        # REGISTER Form
        self.register_username = TextField(
            **self.AppStyle.input_textfield(),
            prefix_icon=icons.ACCOUNT_CIRCLE,
            label=dictionary['username'],
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_email = EmailRow(lambda e: self.activate_lock(), self.page.theme_mode)

        self.register_password = TextField(
            **self.AppStyle.input_textfield(),
            label=dictionary['password'],
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_confirm_password = TextField(
            **self.AppStyle.input_textfield(),
            label=dictionary['confirm_password'],
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_change=lambda e: self.validate()
        )
        self.register_button = ElevatedButton(
            **self.AppStyle.sign_up(),
            disabled=True,
            on_click=lambda e: self.register(),
        )
        self.register_error = SnackBar(
            Text(dictionary['error'], color=colors.WHITE),
            bgcolor=colors.RED)

        self.content = Column(
            controls=[
                Container(
                        content=self.lock,
                        alignment=alignment.center,
                ),
                Row([
                    Text(**self.AppStyle.logo()),
                    ],
                    alignment=MainAxisAlignment.CENTER),

                Container(
                    content=Column([
                        Row([self.register_username,]),
                        self.register_email,
                        Row([self.register_password,]),
                        Row([self.register_confirm_password,]),
                        Row([self.register_button], alignment=MainAxisAlignment.CENTER),
                        Divider(height=20, color=colors.TRANSPARENT),
                        Row([Text("Back to ", size=15,
                             spans=[
                                 TextSpan(
                                     text='Login...',
                                     on_click=lambda s: self.to_login(),
                                     style=TextStyle(
                                         italic=True,
                                         decoration=TextDecoration.UNDERLINE,
                                         size=16)
                                     )
                                 ])
                             ], alignment=MainAxisAlignment.CENTER)
                        ],
                        spacing=10),
                    padding=padding.only(left=15, right=15)
                ),
                self.register_error,]
        )

    def register(self):
        email = self.register_email.controls[0].value
        user = self._session.query(User).filter_by(email=email).one_or_none()
        if not user:
            if self.register_password.value == self.register_confirm_password.value:
                new_user = User(username=self.register_username.value,
                                email=self.register_email.controls[0].value,
                                password=generate_password_hash(self.register_password.value,
                                                                method='pbkdf2:sha256',
                                                                salt_length=8)
                                )
                self._session.add(new_user)
                self._session.commit()
                self.page.client_storage.clear()
                self.page.session.set(key="username", value=self.register_username.value)
                self.page.client_storage.set(key='username', value=self.register_username.value)
                self.page.session.set(key="email", value=self.register_email.controls[0].value)
                self.page.client_storage.set(key='email', value=self.register_email.controls[0].value)
                self.lock.stop_animation()
                sleep(0.2)
                self.page.go(f'/home')
            else:
                self.register_error.open = True
                self.register_error.update()
        else:
            self.register_error.content.value = "User with this email already registered, please Login!"
            self.register_error.open = True
            self.register_error.update()

    def validate(self):
        if all([self.register_username.value,
                self.register_email.controls[0].value,
                self.register_password.value,
                self.register_confirm_password.value]):
            self.register_button.disabled = False
            self.register_button.style.bgcolor = self.AppStyle.sign_up_bgcolor
        else:
            self.register_button.disabled = True
        self.page.update()

    def activate_lock(self):
        if not self.activated_lock:
            self.activated_lock = True
            self.lock.animate_lock()

    def to_login(self):
        self.lock.stop_animation()
        self.page.go('/login')
