from flet import (Row,
                  Text,
                  Icon,
                  ScrollMode,
                  Chip,
                  Page,
                  icons)
from core import AppStyle


class Chips(Row):
    def __init__(self, func, theme_mode: Page.theme_mode):
        super().__init__()
        self.scroll = ScrollMode.HIDDEN
        self.spacing = 15
        self.AppStyle = AppStyle(theme_mode)
        self.tags = ['All', 'Favorite', 'Social Media', 'Entertainment', 'Messengers', 'Work', 'Study']
        self.icons = [icons.ALL_INBOX, icons.FAVORITE_BORDER, icons.FACEBOOK, icons.EMOJI_EMOTIONS,
                      icons.MESSENGER, icons.WORK, icons.SCHOOL]
        self.controls = [
            Chip(**self.AppStyle.chip(),
                 label=Text(f'{self.tags[i]}'),
                 leading=Icon(self.icons[i]),
                 on_select=func,
                 selected=True if i == 0 else False)
            for i in range(len(self.tags))
        ]
