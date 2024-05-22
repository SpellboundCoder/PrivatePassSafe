from flet import *
from core import AppStyle
from controls import EmailRow


class Settings(Container):
    def __init__(self, settings_page: Page, session):
        super().__init__(**AppStyle['window'])
        self._session = session
        self.page = settings_page
        self.padding = 20
        self.gradient = LinearGradient(**AppStyle['gradient'])
        self.emails = self.page.client_storage.get('emails_list') \
            if self.page.client_storage.contains_key("emails_list") else []

        # PASSWORD GENERATOR
        self.password_section = Text(value='Choose your preferred options for password generator : ', size=18)
        self.upper_switch = Switch(**AppStyle['switch'],
                                   value=self.page.client_storage.get('Uppercase')
                                   if self.page.client_storage.contains_key('Uppercase') else None,
                                   on_change=lambda e: self.upper(e))
        self.numbers_switch = Switch(**AppStyle['switch'],
                                     value=self.page.client_storage.get('Numbers')
                                     if self.page.client_storage.contains_key('Numbers') else None,
                                     on_change=lambda e: self.numbers(e))
        self.symbols_switch = Switch(**AppStyle['switch'],
                                     value=self.page.client_storage.get('Symbols')
                                     if self.page.client_storage.contains_key('Symbols') else None,
                                     on_change=lambda e: self.symbols(e))
        self.slider = Slider(value=self.page.client_storage.get('Pass_length')
                             if self.page.client_storage.contains_key('Pass_length') else 8,
                             min=8, max=60, on_change=self.update_length,
                             active_color=colors.DEEP_PURPLE_ACCENT_700)
        self.password_length = int(self.slider.value)
        self.password_label = Text(f"Password length: {self.password_length}",
                                   size=18,
                                   weight=FontWeight.BOLD)

        # EMAIL
        self.email_section = Text(value='Save your preferred Emails : ', size=18)
        self.email_textbox = EmailRow(self.on_focus())
        self.d = Dropdown(**AppStyle['dropdown'], options=[
            dropdown.Option(self.emails[i])
            for i in range(len(self.emails))
        ])
        self.add = ElevatedButton(
            **AppStyle['addButton'],
            on_click=lambda e: self.add_clicked())
        self.delete = OutlinedButton(
            **AppStyle['deleteButton'],
            on_click=lambda e: self.delete_clicked())

        # PAGE CONTENT
        self.content = Column([
            Row([self.email_section], alignment=MainAxisAlignment.START),
            Row([self.d], alignment=MainAxisAlignment.CENTER),
            self.email_textbox,
            Row([self.delete, self.add], alignment=MainAxisAlignment.CENTER),
            Divider(height=5, color=colors.BLACK),
            ResponsiveRow([self.password_section], alignment=MainAxisAlignment.START),
            Row([self.password_label, self.slider]),
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
        ])

    def find_option(self, option_name):
        for option in self.d.options:
            if option_name == option.key:
                return option
        return None

    def add_clicked(self):
        if self.page.client_storage.contains_key("emails_list"):         # True if the key exists
            self.emails.append(self.email_textbox.controls[0].value)
            self.page.client_storage.set("emails_list", self.emails)
        else:
            self.page.client_storage.set('emails_list', [])
        self.d.options.append(dropdown.Option(self.email_textbox.controls[0].value))
        self.d.value = self.email_textbox.controls[0].value
        self.email_textbox.controls[0].value = ""
        self.page.update()

    def delete_clicked(self):
        option = self.find_option(self.d.value)
        if option is not None:
            self.d.options.remove(option)
            self.emails.remove(self.d.value)
            self.page.client_storage.set("emails_list", self.emails)
            # d.value = None
            self.page.update()

    def update_length(self, e: ControlEvent):
        self.password_length = int(e.control.value)
        self.password_label.value = f"Password length: {self.password_length}"
        self.page.client_storage.set('Pass_length', int(e.control.value))
        self.password_label.update()

    def upper(self, e):
        self.page.client_storage.set('Uppercase', e.control.value)

    def numbers(self, e):
        self.page.client_storage.set('Numbers', e.control.value)

    def symbols(self, e):
        self.page.client_storage.set('Symbols', e.control.value)

    def on_focus(self):
        pass
