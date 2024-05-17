from typing import Any

from flet import *

from core.dictionary import *

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 740

# window_style
window_style: dict[str, Any] = {
        'width': 420,
        'height': 740,
        'padding': 10
}
gradient: dict[str, Any] = {
        'begin': alignment.top_center,
        'end': alignment.bottom_center,
        'colors': ['#211951', colors.BLACK87]
}
# Login_title
login_title_margin = margin.only(top=230)
login_title_color: str = "#ffffff"

# login_error
login_error_color: str = '#ff0000'
login_error_bg: str = '#1e1c20'

# Form_Style
form_style: dict[str, Any] = {
        'padding': 15,
        'width': 400,
        'height': 450,
        'bgcolor': colors.TRANSPARENT,
        'border': border.all(4, 'transparent'),
        'border_radius': 10,
        'margin': margin.only(top=5),
}
# Tabs style
tabs_style: dict[str, Any] = {
        'width': 400,
        'height': 445,
        'margin': margin.only(top=215),
        'alignment': alignment.center
}
# input style
input_textfield_style = {
        'bgcolor': '#1d1b1f',
        'width': 340,
        'height': 40,
        'border_color': '#272627',
        'border': 2,
        'border_radius': 10,
        'color': colors.WHITE,
        'text_size': 14,
        'focused_border_color': '#211951',
}
# ElevatedButton   # 'button_border': BorderSide(3, "#272627"), # '#211C6A'
ElevatedButton_Style: dict[str, Any] = {
        'width':  250,
        'height':  40,
        'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.DEEP_PURPLE_ACCENT_700,
        )
}

# bottom_Appbar
appbar_style: dict = {
        'shape': NotchShape.AUTO,
        'bgcolor': colors.BLACK87,
        'height': 60,
        'padding': padding.only(10, 0, 10, 5),
}

# SearchBar
search_bar_style: dict[str, Any] = {
        'view_elevation': 4,
        'width': 365,
        'height': 40,
        'divider_color': colors.BLACK,
        'bar_hint_text': dic_searchbar_bar_hint_text,
        'view_hint_text': dic_searchbar_view_hint_text,
}

# FloatingActionButton
floating_button: dict[str, Any] = {
        'height': 55,
        'width': 55,
        'bgcolor': colors.DEEP_PURPLE_ACCENT_700,
        'icon': icons.ADD,
}
# List Tiles
listTiles: dict[str, Any] = {
        'bgcolor': colors.BLACK38,
        'hover_color': colors.DEEP_PURPLE_ACCENT_400,
        'shape': RoundedRectangleBorder(radius=15),
}

# Column for Tiles
columnTiles: dict[str, Any] = {
        'height': 400,
        'width': 350,
        'spacing': 15,

}

# ListTiles Wrapper(container)
listTilesCard: dict[str, Any] = {
        'height': 400,
        'width': 380,
        'bottom': 130,
        'variant': CardVariant.OUTLINED,
        # 'color': '#211951'
}

