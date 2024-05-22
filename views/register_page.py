from flet import (Container,
                  LinearGradient,
                  TextField,
                  ElevatedButton,
                  SnackBar,
                  Text,
                  Row,
                  Column,
                  FontWeight,
                  MainAxisAlignment,
                  Page,
                  colors,
                  icons,
                  alignment,
                  padding)
from controls import AnimatedLock, EmailRow
from core import AppStyle
from core.dictionary import *
from math import pi
from werkzeug.security import generate_password_hash
from data.dbconfig import User


class Register(Container):
    def __init__(self, login_page: Page, session): # noqa
        super().__init__(**AppStyle['login/register_window'])
        self.page = login_page
        self._session = session
        self.lock = AnimatedLock(rotate_angle=pi / 4)
        self.activated_lock = False
        self.gradient = LinearGradient(**AppStyle['gradient'])

        # REGISTER Form
        self.register_username = TextField(
            **AppStyle['input_textfield'],
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            label=dic_input_register_username,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_email = EmailRow(lambda e: self.activate_lock())

        self.register_password = TextField(
            **AppStyle['input_textfield'],
            label=dic_input_register_password,
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_confirm_password = TextField(
            **AppStyle['input_textfield'],
            label=dic_input_register_confirm_password,
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_change=lambda e: self.validate()
        )
        self.register_button = ElevatedButton(
            **AppStyle['signupButton'],
            disabled=True,
            on_click=lambda e: self.register(),
        )
        self.register_error = SnackBar(
            Text(dic_register_error, color=colors.WHITE),
            **AppStyle['snack_bar'])

        self.content = Column(
            controls=[
                Container(
                        content=self.lock,
                        alignment=alignment.center,
                ),
                Row(
                    controls=[
                        Text(
                            value='Welcome to PrivatePassSafe!',
                            size=22,
                            weight=FontWeight.BOLD),
                        ],
                    alignment=MainAxisAlignment.CENTER),

                Container(
                    content=Column([
                        Row([self.register_username,]),
                        self.register_email,
                        Row([self.register_password,]),
                        Row([self.register_confirm_password,]),
                        Row([self.register_button], alignment=MainAxisAlignment.CENTER)
                        ],
                        spacing=10),
                    **AppStyle['form']
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
                self.page.session.set(key="logged_in", value=user.username)
                self.page.go(f'{self.page.session.get('logged_in')}/dashboard')
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
            self.register_button.style.bgcolor = colors.DEEP_PURPLE_ACCENT_700
        else:
            self.register_button.disabled = True
        self.page.update()

    def activate_lock(self):
        if not self.activated_lock:
            self.activated_lock = True
            self.lock.animate_lock()
