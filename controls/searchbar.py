from flet import Stack, SearchBar, ListTile, Icon, Text

from core import *


# TODO: implement voice Search


class UserSearchBar(Stack):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def close_anchor(self, e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        self.controls[0].close_view(text)

    def handle_change(self, e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(self, e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(self, e):
        print(f"handle_tap")

    def build(self):
        return SearchBar(
            **search_bar_style,
            bar_leading=Icon(name=icons.SEARCH),
            bar_trailing=[Icon(name=icons.MIC)],
            on_change=lambda e: self.handle_change(e),
            on_submit=lambda e: self.handle_submit(e),
            on_tap=lambda e: self.handle_tap(e),
            controls=[
                ListTile(title=Text(f"Color {i}"), on_click=self.close_anchor, data=i)
                for i in range(10)
            ],
        )
