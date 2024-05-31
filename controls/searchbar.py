from flet import (Container,
                  IconButton,
                  Icon,
                  Column,
                  Row,
                  TextField,
                  Text,
                  MainAxisAlignment,
                  SnackBar,
                  AlertDialog,
                  Page,
                  colors,
                  icons)
from core import dict_en, AppStyle
import speech_recognition as sr

dictionary = dict_en['Search']


class UserSearchBar(Container):
    def __init__(self, func, theme_mode: Page.theme_mode):
        super().__init__(**AppStyle(theme_mode).search_bar())

        self.login_error = SnackBar(
            Text(dictionary['error'], color=colors.WHITE),
            bgcolor=colors.RED
        )

        self.dlg = AlertDialog(
           title=Text("Listening..."),
        )

        self.content = Column([
            Row([
                IconButton(icon=icons.ARROW_BACK_ROUNDED, on_click=lambda e: self.view_search_close(),
                           ),
                TextField(
                    **AppStyle(None).search_bar_textfield(),
                    on_change=func,
                ),
                IconButton(icon=icons.CLOSE, icon_size=16, on_click=lambda e: self.clear_search_field(e, func)),
            ], spacing=0, visible=False
            ),
            Row([
                Container(
                    content=Row([
                        Icon(name=icons.SEARCH),
                        Text('Search...', size=18),
                    ], spacing=10),
                    expand=True,
                    on_click=lambda e: self.view_search()
                ),
                IconButton(icon=icons.MIC, icon_size=20,
                           on_click=lambda e: self.recognize_speech_from_microphone()),
            ])
        ], alignment=MainAxisAlignment.CENTER)

    def view_search(self):
        self.content.controls[0].visible = True
        self.content.controls[1].visible = False
        self.update()

    def view_search_close(self):
        self.content.controls[1].visible = True
        self.content.controls[0].visible = False
        self.update()

    def clear_search_field(self, e, func):
        self.content.controls[0].controls[1].value = ''
        self.content.controls[0].controls[1].focus()
        self.content.controls[0].controls[1].update()
        func(e)

    def recognize_speech_from_microphone(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        self.page.dialog = self.dlg

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            self.dlg.open = True
            self.page.update()
            audio = recognizer.listen(source)

        try:
            recognized_text = recognizer.recognize_vosk(audio)
            x = recognized_text.strip(' "{}').split(':')[1].replace('"', '').strip()
            self.content.controls[0].visible = True
            self.content.controls[1].visible = False
            self.content.controls[0].controls[1].value = x
            self.dlg.open = False
            self.page.update()
        except sr.UnknownValueError:
            self.dlg.open = False
            self.login_error.open = True
            self.page.update()
        except sr.RequestError:
            self.dlg.open = False
            self.login_error.open = True
            self.page.update()
