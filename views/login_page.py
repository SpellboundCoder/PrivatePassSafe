from math import pi

from flet import (Page, Container, LinearGradient, Stack, Row, Column, ElevatedButton, SnackBar, Text, Tabs, Tab,
                  FontWeight, CrossAxisAlignment, AnimationCurve,
                  alignment, icons, transform, animation, MainAxisAlignment)
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

from controls import UserInputField, AnimatedLock
from core import *
from data.models import User, engine

Session = sessionmaker(bind=engine)
session = Session()


class Login(Container):
    def __init__(self, login_page: Page): # noqa
        super().__init__()
        # TODO: instead of GIF create an animation of safe lock
        self.lock = AnimatedLock(rotate_angle=pi / 4)
        self.activated_lock = False
        self.gradient = LinearGradient(**gradient)
        self.width = 420
        self.height = 740

        # REGISTER Form
        self.register_username = UserInputField(
            **input_textfield_style,
            prefix_icon=icons.ADMIN_PANEL_SETTINGS,
            label=dic_input_register_username,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_email = UserInputField(
            **input_textfield_style,
            unique_key='register_form',
            prefix_icon=icons.EMAIL,
            label=dic_input_register_email,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.get_suffix_emails(e, self.register_email_suffix)
        )
        self.register_email_suffix = self.suffix_email_containers(self.register_email)

        self.register_password = UserInputField(
            **input_textfield_style,
            label=dic_input_register_password,
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.validate()
        )
        self.register_confirm_password = UserInputField(
            **input_textfield_style,
            label=dic_input_register_confirm_password,
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_change=lambda e: self.validate()
        )
        self.register_button = ElevatedButton(
            **ElevatedButton_Style,
            text=dic_register_button,
            disabled=True,
            on_click=lambda e: self.register(),
        )

        self.register_error = SnackBar(
            Text(dic_register_error, color=login_error_color),
            bgcolor=login_error_bg
        )

        # LOGIN Form
        self.login_email = UserInputField(
            unique_key='login_form',
            **input_textfield_style,
            label=dic_input_login_email,
            prefix_icon=icons.EMAIL,
            on_focus=lambda e: self.activate_lock(),
            on_change=lambda e: self.get_suffix_emails(e, self.login_email_suffix),
        )
        self.login_email_suffix = self.suffix_email_containers(self.login_email)

        self.login_password = UserInputField(
            **input_textfield_style,
            label=dic_input_login_password,
            prefix_icon=icons.LOCK,
            password=True,
            can_reveal_password=True,
            on_focus=lambda e: self.activate_lock()
            # on_change=lambda e:
        )
        self.login_button = ElevatedButton(
            ** ElevatedButton_Style,
            text=dic_login_button,
            on_click=lambda e: self.login_auth(),
        )
        self.login_error = SnackBar(
            Text(dic_login_error, color=login_error_color),
            bgcolor=login_error_bg
        )

        # PAGE CONTENT
        self.content = Container(
            content=Stack(
                controls=[
                    self.login_error,
                    self.register_error,
                    Container(
                        content=self.lock,
                        alignment=alignment.center,
                        margin=margin.only(top=-500)
                              ),
                    Container(
                        Container(
                            Tabs(
                                selected_index=0,
                                animation_duration=300,
                                tabs=[
                                    Tab(
                                        text="Login",
                                        icon=icons.VERIFIED_USER,
                                        content=Container(
                                            content=Column([
                                                Row(controls=[self.login_email,
                                                              self.login_email_suffix],
                                                    spacing=20, alignment=MainAxisAlignment.CENTER),
                                                self.login_password,
                                                Row([self.login_button], alignment=MainAxisAlignment.CENTER)],
                                                spacing=20),
                                            **form_style
                                        )
                                    ),
                                    Tab(
                                        text="Register",
                                        icon=icons.APP_REGISTRATION,
                                        content=Container(
                                            content=Column([
                                                self.register_username,
                                                Row(controls=[self.register_email,
                                                              self.register_email_suffix],
                                                    spacing=20, alignment=MainAxisAlignment.CENTER),
                                                self.register_password,
                                                self.register_confirm_password,
                                                Row([self.register_button], alignment=MainAxisAlignment.CENTER)],
                                                spacing=20),
                                            **form_style
                                        )
                                    )
                                ],
                                expand=1
                            ),
                            **tabs_style
                        ),
                        alignment=alignment.center)
                ])
        )

    def suffix_email_containers(self, field: UserInputField) -> Row:
        email_labels = ["@gmail.com", '@yahoo.com']
        label_title = ["GMAIL", "YAHOO"]
        __ = Row(spacing=1, alignment=MainAxisAlignment.END)
        for index, label in enumerate(email_labels):
            __.controls.append(
                Container(
                    width=45,
                    height=30,
                    alignment=alignment.center,
                    data=label,
                    on_click=lambda e: self.return_email_suffix(e, field=field),
                    content=Text(
                        label_title[index],
                        size=12,
                        weight=FontWeight.BOLD
                    )
                )
            )
        return Row(
            vertical_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.END,
            spacing=2,
            opacity=0,
            animate_opacity=200,
            offset=transform.Offset(0.35, 0),
            animate_offset=animation.Animation(400, curve=AnimationCurve.DECELERATE),
            controls=[__],
        )

    def return_email_suffix(self, e, field: UserInputField) -> None:
        email = field.value
        # self.content.content.controls[1].content.content.tabs[0].content.content.controls[0].controls[0].value
        if e.control.data in email:
            pass
        else:
            if field.unique_key == 'login_form':
                field.value += e.control.data
                self.login_email_suffix.offset = transform.Offset(0.5, 0)
                self.login_email_suffix.opacity = 0
                self.page.update()
            elif field.unique_key == 'register_form':
                field.value += e.control.data
                self.register_email_suffix.offset = transform.Offset(0.5, 0)
                self.register_email_suffix.opacity = 0
                self.page.update()

    def get_suffix_emails(self, e, email_suffix: Row) -> None:
        email = e.data
        if e.data:
            if "@gmail.com" in email or "@yahoo.com" in email:
                email_suffix.offset = transform.Offset(0, 0)
                email_suffix.opacity = 0
                self.page.update()
            else:
                email_suffix.offset = transform.Offset(-1.3, 0)
                email_suffix.opacity = 1
                self.page.update()
        else:
            email_suffix.offset = transform.Offset(0.5, 0)
            email_suffix.opacity = 0
            self.page.update()

    def login_auth(self):
        email = self.login_email.value
        password = self.login_password.value
        user = session.query(User).filter_by(email=email).one_or_none()  # (email=email).first()
        if user:
            if check_password_hash(user.password, password):
                self.page.session.set(key="logged_in", value=user.username)
                self.page.go(
                    f'{user.username}/dashboard'
                )
            else:
                self.login_error.open = True
                self.login_error.update()
        else:
            self.login_error.open = True
            self.login_error.update()

    def register(self):
        email = self.register_email.value
        user = session.query(User).filter_by(email=email).one_or_none()
        if not user:
            if self.register_password.value == self.register_confirm_password.value:
                new_user = User(username=self.register_username.value,
                                email=self.register_email.value,
                                password=generate_password_hash(self.register_password.value,
                                                                method='pbkdf2:sha256',
                                                                salt_length=8)
                                )
                session.add(new_user)
                session.commit()
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
        if all([self.register_username.value, self.register_email.value, self.register_password.value,
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
