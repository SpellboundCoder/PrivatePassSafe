from flet import *
from core import AppStyle


class Settings(Container):
    def __init__(self, settings_page: Page, session):
        super().__init__(**AppStyle['window'])
        self._session = session
        self.page = settings_page
        self.gradient = LinearGradient(**AppStyle['gradient'])

