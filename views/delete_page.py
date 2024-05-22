from flet import *
from core import *
from controls import UserSearchBar


class Delete(Container):
    def __init__(self, delete_page: Page, session):
        super().__init__()
        self.page = delete_page
        self._session = session
        self.search_bar = UserSearchBar(lambda e: self.filter_panel(e))
        self.expand = True
        self.padding = 10
        self.gradient = LinearGradient(**AppStyle['gradient'])
        self.panels = ExpansionPanelList(
            expand_icon_color=colors.DEEP_PURPLE_ACCENT_700,
            elevation=8,
            divider_color=colors.DEEP_PURPLE_ACCENT_700,
            on_change=lambda e: self.handle_change(e),
            controls=[
                # ExpansionPanel(
                #     # has no header and content - placeholders will be used
                #     expanded=True)
                ]
            )

        for i in range(10):
            exp = ExpansionPanel(
                header=ListTile(title=Text(f"Panel {i}")),
            )
            exp.content = ListTile(
                title=Text(f"This is in Panel {i}"),
                subtitle=Text(f"Press the icon to delete panel {i}"),
                trailing=IconButton(icons.DELETE, on_click=self.handle_delete, data=exp),
            )
            self.panels.controls.append(exp)

        self.content = Column(
            controls=[Text(value='PrivatePassSafe', color=colors.RED_ACCENT_700, size=25, weight=FontWeight.BOLD),
                      self.search_bar,
                      self.panels],
            scroll=ScrollMode.HIDDEN,
            spacing=15
        )

    def handle_change(self, e: ControlEvent):
        print(f"change on panel with index {e.data}")

    def handle_delete(self, e: ControlEvent):
        self.panels.controls.remove(e.control.data)
        self.page.update()

    def filter_panel(self, e):
        if e.data:
            for panel in self.panels.controls:
                panel.visible = (
                    True
                    if e.data in panel.content.title.value
                    else False
                )
                self.panels.update()
        else:
            for panel in self.panels.controls:
                panel.visible = True
                self.panels.update()
