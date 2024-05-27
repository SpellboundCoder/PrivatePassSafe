from flet import (SearchBar,
                  IconButton,
                  Icon,
                  RoundedRectangleBorder,
                  icons)
from core import AppStyle

# TODO: implement voice Search


class UserSearchBar(SearchBar):
    def __init__(self, func, *args):
        super().__init__(*args, **AppStyle['search_bar'])
        self.view_shape = RoundedRectangleBorder(radius=10)
        self.bar_leading = Icon(name=icons.SEARCH)
        self.bar_trailing = [IconButton(icon=icons.CLOSE), IconButton(icon=icons.MIC)]
        self.on_change = lambda e: func(e)
        self.on_tap = lambda e: func(e)

