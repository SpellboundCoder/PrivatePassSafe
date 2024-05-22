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
                  colors,
                  icons,
                  PopupMenuButton,
                  PopupMenuItem,
                  Stack,
                  Dropdown,
                  Image,
                  dropdown
                  )
from core import AppStyle
from func import generate_password


class Add(Container):
    def __init__(self, add_page: Page, session):
        super().__init__(**AppStyle['window'])
        self._session = session
        self.page = add_page
        self.padding = 20
        self.gradient = LinearGradient(**AppStyle['gradient'])
        self.password_textfield = TextField(**AppStyle['password_field'])

        self.slider = Slider(value=self.page.client_storage.get('Pass_length')
                             if self.page.client_storage.contains_key('Pass_length') else 10,
                             min=8, max=60, on_change=self.update_length,
                             active_color=colors.DEEP_PURPLE_ACCENT_700
                             )
        self.password_length = int(self.slider.value)
        self.password_label = Text(f"Password length: {self.password_length}",
                                   size=18,
                                   weight=FontWeight.BOLD
                                   )
        self.upper_switch = Switch(**AppStyle['switch'],
                                   value=self.page.client_storage.get('Uppercase')
                                   if self.page.client_storage.contains_key('Uppercase') else None
                                   )
        self.numbers_switch = Switch(**AppStyle['switch'],
                                     value=self.page.client_storage.get('Numbers')
                                     if self.page.client_storage.contains_key('Numbers') else None
                                     )
        self.symbols_switch = Switch(**AppStyle['switch'],
                                     value=self.page.client_storage.get('Symbols')
                                     if self.page.client_storage.contains_key('Symbols') else None
                                     )
        self.lower_switch = Switch(disabled=True, value=True)

        self.email = TextField(**AppStyle['input_textfield'],
                               label="Email")
        self.email_list = self.page.client_storage.get('emails_list') \
            if self.page.client_storage.contains_key("emails_list") else []

        self._dropdown = PopupMenuButton(
            icon=icons.ARROW_DROP_DOWN,
            right=5,
            offset=Offset(0, 0.09),
            # on_change=self.dropdown_changed,
            # PopupMenuItem(content=Image(src='FB.png'), on_click=self.chosen_email)
            items=[
                PopupMenuItem(self.email_list[i], on_click=self.chosen_email)
                for i in range(len(self.email_list))
            ],
        )
        self.icons_dropdown = Dropdown(
            width=100,
            height=100,
            options=[dropdown.Option(icons.SPA)]
            )
        self.content = Column(
            controls=[
                Row([
                    self.icons_dropdown,
                    TextField(**AppStyle['input_textfield'], label="Website", prefix_text="https://"),
                ], spacing=0),
                Row([
                    Icon(icons.ACCOUNT_CIRCLE, size=40),
                    TextField(**AppStyle['input_textfield'], label="Username")
                ], spacing=0),
                Stack([Row([
                    Icon(icons.EMAIL, size=40), self.email,
                ], spacing=0), self._dropdown]),
                Row([
                    Icon(icons.PHONE, size=40),
                    TextField(**AppStyle['input_textfield'], label="Mobile"),
                ], spacing=0),
                Row([
                    Icon(icons.PASSWORD, size=40),
                    Text('Your Password:', size=20, weight=FontWeight.BOLD),
                ], spacing=0, alignment=MainAxisAlignment.CENTER),
                self.password_textfield,
                Row([
                    self.password_label,
                    IconButton(
                        icon=icons.LOCK_RESET,
                        icon_size=40,
                        icon_color=colors.DEEP_PURPLE_ACCENT_700,
                        offset=Offset(0, -0.2),
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
                    ElevatedButton(**AppStyle['submitButton']),
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    ElevatedButton(**AppStyle['cancelButton'],
                                   on_click=lambda e: self.back_home())
                ], alignment=MainAxisAlignment.CENTER)
            ],
            scroll=ScrollMode.HIDDEN)

    def update_length(self, e: ControlEvent):
        self.password_length = int(e.control.value)
        self.password_label.value = f"Password length: {self.password_length}"
        self.password_label.update()

    def create_password(self):
        self.password_textfield.value = generate_password(length=self.password_length,
                                                          upper=self.upper_switch.value,
                                                          num=self.numbers_switch.value,
                                                          punc=self.symbols_switch.value
                                                          )
        self.password_textfield.update()

    def chosen_email(self, e):
        self.email.value = e.control.text
        self.page.update()

    def back_home(self):
        self.page.go('/home')

