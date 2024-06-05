from flet import (Container,
                  Page,
                  LinearGradient,
                  TextField,
                  Slider,
                  Text,
                  FontWeight,
                  Switch,
                  Column,
                  Row,
                  Icon,
                  IconButton,
                  MainAxisAlignment,
                  Offset,
                  ElevatedButton,
                  ControlEvent,
                  ScrollMode,
                  icons,
                  PopupMenuButton,
                  PopupMenuItem,
                  Stack,
                  Image,
                  Dropdown,
                  TextButton,
                  AlertDialog,
                  dropdown,
                  )
from core import dict_en, AppStyle
from func import generate_password, Encryption
import datetime as dt
from data.dbconfig import User, Website


now = dt.datetime.now().strftime('%d-%m-%y (%I-%M %p)')
dictionary = dict_en['Add']


class Update(Container):
    def __init__(self, update_page: Page, session):
        super().__init__(padding=20, expand=True)
        self.db_session = session
        self.page = update_page

        self.AppStyle = AppStyle(self.page.theme_mode)
        self.Encryption = Encryption(self.page.session.get('pass'))
        self.gradient = LinearGradient(**self.AppStyle.gradient())

        # DATA
        self.user = session.query(User).filter_by(email=self.page.session.get('email')).one_or_none()
        self.websites = self.user.websites

        # WEBSITE
        self.icon = Image(src='/icons/icon0.png', width=40, height=45, border_radius=15, offset=Offset(0, -0.03))
        self.chose_website_id = None
        self.website_options = Dropdown(
            **self.AppStyle.dropdown(),
            hint_text='Pick a Website',
            on_change=lambda e: self.update_fields(e),
            options=[
                dropdown.Option(f"{website.website}", data=website)
                for website in self.websites
            ],
        )

        # USERNAME
        self.username = TextField(**self.AppStyle.input_textfield(), label="Username")

        # EMAIL
        self.email = TextField(**self.AppStyle.input_textfield(), label='Email')
        self.email_list = self.page.client_storage.get('emails_list') \
            if self.page.client_storage.contains_key('emails_list') else []
        self._dropdown = PopupMenuButton(
            icon=icons.ARROW_DROP_DOWN,
            right=0,
            offset=Offset(0, 0.09),
            items=[
                PopupMenuItem(self.email_list[i], on_click=self.chosen_email)
                for i in range(len(self.email_list))
            ],
        )

        # PASSWORD
        self.password_textfield = TextField(**self.AppStyle.password_field())
        self.slider = Slider(
            value=self.page.client_storage.get('Pass_length')
            if self.page.client_storage.contains_key('Pass_length') else 10,
            on_change=self.update_length,
            **self.AppStyle.slider())

        self.password_length = int(self.slider.value)
        self.password_label = Text(
            f"Password length: {self.password_length}",
            size=18,
            weight=FontWeight.BOLD)
        self.upper_switch = Switch(
            **self.AppStyle.switch(),
            value=self.page.client_storage.get('Uppercase')
            if self.page.client_storage.contains_key('Uppercase') else None)
        self.numbers_switch = Switch(
            **self.AppStyle.switch(),
            value=self.page.client_storage.get('Numbers') if self.page.client_storage.contains_key('Numbers') else None)
        self.symbols_switch = Switch(
            **self.AppStyle.switch(),
            value=self.page.client_storage.get('Symbols') if self.page.client_storage.contains_key('Symbols') else None)
        self.lower_switch = Switch(disabled=True, value=True)

        # TAGS
        self.tag_list = ["Favorite", "Entertainment", "Social Media", "Messengers", "Work", "Study", "Other"]
        self.dd_tags = Dropdown(
            **self.AppStyle.dropdown(),
            value='Other',
            options=[
                dropdown.Option(f'{self.tag_list[i]}')
                for i in range(len(self.tag_list))
            ],
        )
        # MOBILE
        self.mobile = TextField(**self.AppStyle.input_textfield(), label="Mobile")

        # DIALOG
        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Please confirm"),
            content=Text("Are you sure you wanna update info ?"),
            actions=[
                TextButton("Yes", on_click=lambda e: self.confirm_updates()),
                TextButton("No", on_click=lambda e: self.close_dlg()),
            ],
            actions_alignment=MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        self.content = Column(
            controls=[
                Text('Select a website you wanna make changes:', size=20, weight=FontWeight.BOLD),
                Row([
                    self.icon,
                    self.website_options
                ], spacing=2),
                Row([
                    Icon(icons.ACCOUNT_CIRCLE, **self.AppStyle.icon()),
                    self.username
                ], spacing=0),
                Stack([
                    Row([
                        Icon(icons.EMAIL, **self.AppStyle.icon()), self.email,
                    ], spacing=0), self._dropdown]),
                Row([
                    Icon(icons.PHONE, **self.AppStyle.icon()), self.mobile,
                ], spacing=0),
                Row([
                    Icon(icons.TAG, **self.AppStyle.icon()), self.dd_tags,
                ], spacing=0),

                Row([
                    Icon(icons.PASSWORD, **self.AppStyle.icon()),
                    Text('Your Password:', size=20, weight=FontWeight.BOLD),
                ], spacing=0, alignment=MainAxisAlignment.CENTER),
                self.password_textfield,
                Row([
                    self.password_label,
                    IconButton(
                        **self.AppStyle.generate_pass_icon(),
                        on_click=lambda e: self.create_password()
                    )],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    height=50),
                self.slider,
                Row(height=40, controls=[
                    Text('Uppercase(A-Z)', size=18, weight=FontWeight.BOLD),
                    self.upper_switch],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    ),
                Row(height=40, controls=[
                    Text('Numbers(123...)', size=18, weight=FontWeight.BOLD),
                    self.numbers_switch,
                ], alignment=MainAxisAlignment.SPACE_BETWEEN, ),
                Row(height=40, controls=[
                    Text('Random Symbols($&*...)', size=18, weight=FontWeight.BOLD),
                    self.symbols_switch,
                ], alignment=MainAxisAlignment.SPACE_BETWEEN, ),
                Row(height=40, controls=[
                    Text('Lowercase(a-z)', size=18, weight=FontWeight.BOLD),
                    self.lower_switch,
                ], alignment=MainAxisAlignment.SPACE_BETWEEN, ),
                Row(controls=[
                    ElevatedButton(
                        text='Update',
                        **self.AppStyle.primary_button(),
                        on_click=lambda e: self.open_dlg_modal())
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    ElevatedButton(
                        **self.AppStyle.cancel_button(),
                        on_click=lambda e: self.back_home())
                ], alignment=MainAxisAlignment.CENTER),
            ],
            scroll=ScrollMode.HIDDEN)

    def confirm_updates(self):
        website = self.db_session.query(Website).filter_by(id=self.chose_website_id).one_or_none()
        website.icon = self.icon.src
        website.tag = self.dd_tags.value
        website.email = self.Encryption.encrypt_data(self.email.value)
        website.password = self.Encryption.encrypt_data(self.password_textfield.value)
        website.date = now
        if self.username.value:
            website.username = self.Encryption.encrypt_data(self.username.value)
        if self.mobile.value:
            website.mobile = self.Encryption.encrypt_data(self.mobile.value)
        self.db_session.commit()
        self.page.go('/home')

    def update_length(self, e: ControlEvent):
        self.password_length = int(e.control.value)
        self.password_label.value = f"Password length: {self.password_length}"
        self.password_label.update()

    def create_password(self):
        self.password_textfield.value = generate_password(
            length=self.password_length,
            upper=self.upper_switch.value,
            num=self.numbers_switch.value,
            punc=self.symbols_switch.value
        )
        self.password_textfield.update()

    def chosen_email(self, e):
        self.email.value = e.control.text
        self.email.update()

    def update_fields(self, e):
        for option in e.control.options:
            if e.control.value == option.key:
                self.icon.src = option.data.icon
                self.username.value = self.Encryption.decrypt_data(option.data.username) if option.data.username else ""
                self.email.value = self.Encryption.decrypt_data(option.data.email)
                self.mobile.value = self.Encryption.decrypt_data(option.data.mobile) if option.data.mobile else ""
                self.password_textfield.value = self.Encryption.decrypt_data(option.data.password)
                self.dd_tags.value = option.data.tag
                self.chose_website_id = option.data.id
                self.update()

    def back_home(self):
        self.page.go('/home')

    def open_dlg_modal(self):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def close_dlg(self):
        self.dlg_modal.open = False
        self.page.update()
