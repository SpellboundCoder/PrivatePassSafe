from flet import (Container,
                  Page,
                  LinearGradient,
                  ExpansionPanelList,
                  ExpansionPanel,
                  ListTile,
                  Text,
                  Image,
                  IconButton,
                  Column,
                  ControlEvent,
                  FontWeight,
                  ScrollMode,
Theme,
ExpansionTileTheme,
                  icons,
                  colors)
from core import AppStyle
from controls import UserSearchBar
from data.dbconfig import User


class Delete(Container):
    def __init__(self, delete_page: Page, session):
        super().__init__(expand=True, padding=20)
        self.page = delete_page
        self.db_session = session
        self.AppStyle = AppStyle(self.page.theme_mode)

        self.user = session.query(User).filter_by(email=self.page.session.get('email')).one_or_none()
        self.websites = self.user.websites
        self.search_bar = UserSearchBar(lambda e: self.filter_panel(e), self.page.theme_mode)

        self.gradient = LinearGradient(**self.AppStyle.gradient())

        self.panels = ExpansionPanelList(**self.AppStyle.expansion_panel())

        for website in self.websites:
            exp = ExpansionPanel(
                header=ListTile(
                    title=Text(f"{website.website}"),
                    leading=Image(src=website.icon),
                    data=website),

            )
            exp.content = ListTile(
                title=Text(f"Email: {website.email}"),
                subtitle=Text(f"Password {website.password}"),
                trailing=IconButton(icons.DELETE, on_click=lambda e: self.handle_delete(e), data=exp,
                                    icon_color=colors.RED_ACCENT_700),
            )
            self.panels.controls.append(exp)

        self.content = Column(
            controls=[Text(value='PrivatePassSafe', color=colors.RED_ACCENT_700, size=25, weight=FontWeight.BOLD),
                      self.search_bar,
                      Container(content=self.panels, padding=10)],
            scroll=ScrollMode.HIDDEN,
            spacing=15
        )

    def handle_delete(self, e: ControlEvent):
        website_to_delete = e.control.data.header.data
        self.db_session.delete(website_to_delete)
        self.db_session.commit()
        self.panels.controls.remove(e.control.data)
        self.page.update()

    def filter_panel(self, e):
        if e.data:
            for panel in self.panels.controls:
                panel.visible = (
                    True
                    if e.data in panel.header.title.value
                    else False
                )
                self.panels.update()
        else:
            for panel in self.panels.controls:
                panel.visible = True
                self.panels.update()
