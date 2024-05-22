from flet import Stack, SearchBar, ListTile, Icon, Text
from typing import Callable
from core import *

# TODO: implement voice Search

# SearchBar()
class UserSearchBar(SearchBar):
    def __init__(self, func, *args):
        super().__init__(*args, **AppStyle['search_bar'])
        self.func = func
        self.view_shape = RoundedRectangleBorder(radius=10)
        self.bar_leading = Icon(name=icons.SEARCH)
        self.bar_trailing = [Icon(name=icons.MIC)]
        self.on_change = lambda e: self.func(e)
        self.on_submit = lambda e: self.handle_submit(e)
        self.on_tap = lambda e: self.handle_tap(e)

        self.controls = [
            ListTile(title=Text(f"Color {i}"), on_click=self.close_anchor, data=i)
            for i in range(2)
        ]

    def close_anchor(self, e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        self.controls[0].close_view(text)

    def handle_submit(self, e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(self, e):
        self.close_view()
        # self.bar_trailing = [IconButton(icon=icons.CLOSE,
        #                                 on_click=lambda e: self.clear_searchbar(e))]

    # def clear_searchbar(self, e):
    #     e.data = None
    #     self.update()

    # def build(self) -> SearchBar:
    #     return SearchBar(
    #         **AppStyle['search_bar'],
    #         bar_leading=Icon(name=icons.SEARCH),
    #         bar_trailing=[Icon(name=icons.MIC)],
    #         on_change=lambda e: self.func,
    #         on_submit=lambda e: self.handle_submit(e),
    #         on_tap=lambda e: self.handle_tap(e),
    #         controls=[
    #             ListTile(title=Text(f"Color {i}"), on_click=self.close_anchor, data=i)
    #             for i in range(10)
    #         ],
    #     )
