import os
import shutil
from flet import *
from core import AppStyle
from controls import EmailRow
from func import load_dict, save_dict

dict_path = 'data/dict.json'


class Settings(Container):
    def __init__(self, settings_page: Page, session):
        super().__init__(expand=True, padding=20)
        self._session = session
        self.page = settings_page

        self.AppStyle = AppStyle(self.page.theme_mode)
        self.dict = load_dict(dict_path)['websites']
        self.gradient = LinearGradient(**self.AppStyle.gradient())

        # ACCOUNT
        self.account_info = Text(value='Your account info:', size=18, weight=FontWeight.BOLD)
        self.username = TextField(
            **self.AppStyle.read_only(), value=self.page.client_storage.get('username'), label='Username')
        self.email = TextField(
            **self.AppStyle.read_only(), value=self.page.client_storage.get('email'), label='Email')
        self.log_out_icon = IconButton(icon=icons.LOGOUT, icon_size=40,
                                       on_click=lambda _: self.open_dlg_modal())
        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Please confirm"),
            content=Text("Are you sure yoo want to Logout? All your preferences will be deleted..."),
            actions=[
                TextButton("Yes", on_click=lambda _: self.log_out()),
                TextButton("No", on_click=lambda _: self.close_dlg_modal()),
            ],
            actions_alignment=MainAxisAlignment.END,
            # on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        # UPLOAD
        self.file_picker = FilePicker(on_result=self.pick_files_result)
        self.logo_img = Image(width=40, height=40, src='assets/icons/icon0.png')
        self.upload_label = Text(value="Upload website's logo and enter the name: ",
                                 size=18, weight=FontWeight.BOLD)
        self.upload_textfield = TextField(**self.AppStyle.input_textfield(), hint_text='Website...', label='Website')
        self.upload_icon = IconButton(icon=icons.UPLOAD,
                                      on_click=lambda _: self.file_picker.pick_files(
                                              allowed_extensions=['png'],
                                              file_type=FilePickerFileType.IMAGE
                                      ))
        self.upload_button = ElevatedButton(**self.AppStyle.add_button(), width=25,
                                            on_click=lambda _: self.add_website())
        self.page.overlay.append(self.file_picker)

        # EMAIL
        self.emails = self.page.client_storage.get('emails_list') \
            if self.page.client_storage.contains_key("emails_list") else []
        self.email_section = Text(value='Save your preferred Emails : ', size=18, weight=FontWeight.BOLD)
        self.email_textbox = EmailRow(self.on_focus(), self.page.theme_mode)
        self.d = Dropdown(**self.AppStyle.dropdown(), options=[
            dropdown.Option(self.emails[i])
            for i in range(len(self.emails))
        ])
        self.add = ElevatedButton(
            **self.AppStyle.add_button(),
            on_click=lambda e: self.add_email())
        self.delete = OutlinedButton(
            **self.AppStyle.delete_button(),
            on_click=lambda e: self.delete_clicked())

        # THEME_MODE
        self.dark_mode_icon = IconButton(
            **self.AppStyle.dark_theme_icon(),
            on_click=lambda e: self.change_theme(e),
            )
        self.light_mode_icon = IconButton(
            **self.AppStyle.light_theme_icon(),
            on_click=lambda e: self.change_theme(e),
        )

        # PAGE CONTENT
        self.content = Column([
            Row([self.account_info]),
            Row([self.username, self.email]),
            Row([self.upload_label]),
            Row([self.logo_img, self.upload_icon, self.upload_textfield, self.upload_button]),
            Divider(height=5, color=colors.BLACK),
            Row([self.email_section], alignment=MainAxisAlignment.START),
            Row([self.d], alignment=MainAxisAlignment.CENTER),
            self.email_textbox,
            Row([self.delete, self.add], alignment=MainAxisAlignment.CENTER),
            Divider(height=5, color=colors.BLACK),
            Row(height=50, controls=[
                Text('Chose a Theme Mode: ', size=18, weight=FontWeight.BOLD),
                Container(Row([self.dark_mode_icon, self.light_mode_icon], spacing=0))
            ], alignment=MainAxisAlignment.SPACE_BETWEEN),
            Divider(height=5, color=colors.BLACK),
            Row(height=50, controls=[
                Text('Logout: ', size=18, weight=FontWeight.BOLD),
                self.log_out_icon
            ], alignment=MainAxisAlignment.SPACE_BETWEEN),
            self.file_picker
        ])

    def pick_files_result(self, e: FilePickerResultEvent):
        icons_path = os.path.join(os.getcwd(), 'assets/icons')
        icons_count = len(os.listdir(icons_path))
        for x in e.files:
            # shutil.copy(x.path, icons_path)
            # current_file_path = os.path.join(icons_path, x.name)
            # new_name = f'icon{icons_count}.png'
            # new_file_path = os.path.join(icons_path, new_name)
            # os.rename(current_file_path, new_file_path)
            self.logo_img.src = x.path                   # f'assets/icons/{new_name}'
            self.page.update()

    def find_option(self, option_name):
        for option in self.d.options:
            if option_name == option.key:
                return option
        return None

    def open_dlg_modal(self):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def close_dlg_modal(self):
        self.dlg_modal.open = False
        self.page.update()

    def log_out(self):
        self.page.client_storage.clear()
        self.page.session.clear()
        self.page.go('/login')

    def change_theme(self, e):
        if e.control.icon == icons.DARK_MODE_OUTLINED:
            self.page.client_storage.set("theme", 'DARK')
            self.page.theme_mode = ThemeMode.DARK
            self.page.update()
            self.page.go('/home')
            self.page.go('/settings')
        elif e.control.icon == icons.LIGHT_MODE_OUTLINED:
            self.page.client_storage.set("theme", 'LIGHT')
            self.page.theme_mode = ThemeMode.LIGHT
            self.page.update()
            self.page.go('/home')
            self.page.go('/settings')

    def add_email(self):
        if self.page.client_storage.contains_key("emails_list"):         # True if the key exists
            self.emails.append(self.email_textbox.controls[0].value)
            self.page.client_storage.set("emails_list", self.emails)
        else:
            self.page.client_storage.set('emails_list', [])
        self.d.options.append(dropdown.Option(self.email_textbox.controls[0].value))
        self.d.value = self.email_textbox.controls[0].value
        self.email_textbox.controls[0].value = ""
        self.page.update()

    def add_website(self):
        icons_path = os.path.join(os.getcwd(), 'assets/icons')
        icons_count = len(os.listdir(icons_path))
        for x in self.file_picker.result.files:
            shutil.copy(x.path, icons_path)
            current_file_path = os.path.join(icons_path, x.name)
            new_name = f'icon{icons_count}.png'
            new_file_path = os.path.join(icons_path, new_name)
            os.rename(current_file_path, new_file_path)
        self.dict[f'icon{icons_count}'] = self.upload_textfield.value
        save_dict(self.dict, dict_path)
        self.logo_img.src = 'assets/icons/icon0.png'
        self.upload_textfield.value = ''                  # f'assets/icons/{new_name}'
        self.page.update()

    def delete_clicked(self):
        option = self.find_option(self.d.value)
        if option is not None:
            self.d.options.remove(option)
            self.emails.remove(self.d.value)
            self.page.client_storage.set("emails_list", self.emails)
            # d.value = None
            self.page.update()

    def on_focus(self):
        pass
