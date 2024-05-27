from typing import Any
from flet import *

# window_style
AppStyle: dict[str, dict[str, Any]] = {
    'login/register_window': {
        'padding': 15,
        'expand': True
    },
    'window': {
        'padding': 10,
        'expand': True
    },  # GRADIENT
    'gradient': {
        'begin': alignment.top_center,
        'end': alignment.bottom_center,
        'colors': ['#211951', colors.BLACK87]
    },  # LOGIN
    'snack_bar': {
        'bgcolor': colors.RED,
        # 'action_color': colors.RED
    },  # Form
    'form': {
        'padding': padding.only(15, right=15),
        'expand': True,
    },  # INPUT TEXTFIELD
    'input_textfield': {
        'bgcolor': '#1d1b1f',
        'border_color': colors.BLACK87,
        'border': 2,
        'border_radius': 10,
        'color': colors.WHITE,
        'text_size': 18,
        'focused_border_color': colors.INDIGO,
        'text_vertical_align': -0.2,
        'content_padding': 0,
        'height': 50,
        'expand': True
    },  # Password  Field
    'password_field': {
        'multiline': True,
        'max_lines': 2,
        'min_lines': 1,
        'height': 80,
        'text_align': TextAlign.CENTER,
        'content_padding': 10,
        'bgcolor': '#1d1b1f',
        'border_color': colors.BLACK87,
        'border': 4,
        'border_radius': 10,
        'color': colors.WHITE,
        'text_size': 22,
        'focused_border_color': colors.DEEP_PURPLE_ACCENT_700,
        'text_style': TextStyle(
            weight=FontWeight.BOLD
        )
    },
    'chip': {
        'bgcolor': colors.BLUE_GREY_800,
        'selected_color': colors.DEEP_PURPLE_ACCENT_700,
        'show_checkmark': False,
    },
    # ElevatedButton
    'loginButton': {
        'text': 'Login',
        'height': 45,
        'width': 300,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
        )
    },
    'cancelButton': {
        'text': 'Cancel',
        'height': 45,
        'width': 300,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.RED_ACCENT_700,
        )
    },
    'submitButton': {
        'text': 'Submit',
        'height': 45,
        'width': 300,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
        )
    },
    'signupButton': {
        'text': 'Submit',
        'height': 45,
        'width': 300,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.GREY,
        )
    },  # bottom_Appbar
    'appbar': {
        'shape': NotchShape.AUTO,
        'bgcolor': colors.BLACK87,
        'height': 50,
        'padding': padding.only(10, 0, 10, 0),
    },  # SearchBar
    'search_bar': {
        'view_elevation': 0,
        # 'expand': False,
        'height': 40,
        'divider_color': colors.BLACK,
        'bar_hint_text': "Search a website...",
        # 'view_hint_text': dic_searchbar_view_hint_text,
    },  # FloatingActionButton
    'floating_button': {
        'height': 55,
        'width': 55,
        'bgcolor': colors.DEEP_PURPLE_ACCENT_700,
        'icon': icons.ADD,
    },  # List Tiles
    'listTiles': {
        'bgcolor': colors.BLACK38,
        'hover_color': colors.DEEP_PURPLE_ACCENT_400,
        'adaptive': False
    },  # Column for Tiles
    'columnTiles': {
        'spacing': 15,
    },  # ListTiles Wrapper(container)
    'PasswordsCard': {
        # 'expand': True,
        'shadow_color': colors.WHITE,
        'elevation': 15,
        'variant': CardVariant.OUTLINED,
        'margin': margin.only(left=20, right=20, top=10)
    },  # Switch
    'switch': {
        'active_color': colors.DEEP_PURPLE_ACCENT_700,
        # 'value': False
    },
    'dropdown': {
        'bgcolor': '#1d1b1f',
        'border_color': colors.BLACK87,
        'border': 2,
        'border_radius': 10,
        'color': colors.WHITE,
        'height': 50,
        'expand': True,
        'content_padding': padding.only(bottom=5, left=10),
        'text_style': TextStyle(size=20)
    },
    'addButton': {
        'text': 'add',
        'height': 40,
        'expand': True,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
        )
    },
    'deleteButton': {
        'text': 'delete',
        'height': 40,
        'expand': True,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.RED_ACCENT_700,
        )
    },
    'updateButton': {
        'text': 'Update',
        'height': 45,
        'width': 300,
        'style': ButtonStyle(
            color=colors.WHITE,
            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
        )
    },
    'read_only_textfield': {
        'read_only': True,
        'expand': True,
        'border': InputBorder.UNDERLINE,
    },
    'icon_copy': {
        'icon': icons.COPY,
        'icon_size': 30,
        'offset': Offset(-0.3, 0.1)
    }

}
