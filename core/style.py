from flet import (Page,
                  ThemeMode,
                  FontWeight,
                  TextAlign,
                  TextStyle,
                  InputBorder,
                  VerticalAlignment,
                  ButtonStyle,
                  Offset,
                  CardVariant,
                  BoxShadow,
                  AnimationCurve,
                  NotchShape,
                  padding,
                  colors,
                  icons,
                  margin,
                  alignment,
                  animation)
from typing import Union


class AppStyle:
    def __init__(self, theme_mode: Union[Page.theme_mode, None]):
        super().__init__()
        self.mode = theme_mode
        self.sign_up_bgcolor = colors.DEEP_PURPLE_ACCENT_700 \
            if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700

    # GRADIENT
    def gradient(self) -> dict:
        return {
                'begin': alignment.top_center,
                'end': alignment.bottom_center,
                'colors': ['#211951', colors.BLACK87] if self.mode == ThemeMode.DARK else
                          [colors.LIGHT_BLUE, colors.WHITE]
        }

    # LOGO
    @staticmethod
    def logo() -> dict:
        return {
            'value': 'PrivatePassSafe',
            'size': 18,
            'weight': FontWeight.BOLD
        }

    # TEXT FIELDS
    def input_textfield(self) -> dict:
        return {
            'bgcolor': '#1d1b1f' if self.mode == ThemeMode.DARK else colors.WHITE,
            'border_color': colors.BLACK87,
            'border': 2,
            'border_radius': 10,
            'color': colors.WHITE if self.mode == ThemeMode.DARK else colors.BLACK87,
            'text_size': 18,
            'focused_border_color': colors.INDIGO,
            'text_vertical_align': -0.2,
            'height': 50,
            'expand': True,
            'content_padding': padding.only(left=10)
        }

    def password_field(self) -> dict:
        return {
            'multiline': True,
            'max_lines': 2,
            'min_lines': 1,
            'height': 80,
            'text_align': TextAlign.CENTER,
            'content_padding': 10,
            'bgcolor': '#1d1b1f' if self.mode == ThemeMode.DARK else colors.WHITE,
            'border_color': colors.BLACK87,
            'border': 4,
            'border_radius': 10,
            'color': colors.WHITE if self.mode == ThemeMode.DARK else colors.BLACK87,
            'text_size': 22,
            'focused_border_color': colors.DEEP_PURPLE_ACCENT_700,
            'text_style': TextStyle(
                weight=FontWeight.BOLD
            )
        }

    @staticmethod
    def read_only() -> dict:
        return {
            'read_only': True,
            'expand': True,
            'border': InputBorder.UNDERLINE
        }

    # SEARCH
    @staticmethod
    def search_bar_textfield() -> dict:
        return {
            'bgcolor': colors.TRANSPARENT,
            'border_radius': 20,
            'hint_text': 'Search',
            'text_vertical_align': VerticalAlignment.END,
            'border': InputBorder.NONE,
            'hover_color': colors.TRANSPARENT,
            'expand': True,
            'autofocus': True,
        }

    def search_bar(self) -> dict:
        return {
            'height': 45,
            'bgcolor': colors.GREY_900 if self.mode == ThemeMode.DARK else colors.WHITE70,
            'padding': padding.only(left=10, right=10),
            'margin': margin.only(left=10, right=10),
            'border_radius': 20
        }

    # BUTTONS
    def primary_button(self) -> dict:
        return {
            'height': 45,
            'width': 300,
            'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
            )
        }

    def add_button(self) -> dict:
        return {
            'text': 'Add',
            'height': 40,
            'expand': True,
            'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
            )
        }

    def floating_button(self) -> dict:
        return {
            'height': 55,
            'width': 55,
            'bgcolor': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
            'icon': icons.ADD,
        }

    @staticmethod
    def sign_up() -> dict:
        return {
            'text': 'Sign Up',
            'height': 45,
            'width': 300,
            'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.GREY,
            )
        }

    @staticmethod
    def cancel_button() -> dict:
        return {
            'text': 'Cancel',
            'height': 45,
            'width': 300,
            'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.RED_ACCENT_700,
            )
        }

    @staticmethod
    def delete_button() -> dict:
        return {
            'text': 'Delete',
            'height': 40,
            'expand': True,
            'style': ButtonStyle(
                color=colors.WHITE,
                bgcolor=colors.RED_ACCENT_700,
            )
        }

    # CHIP / SWITCH / SLIDER / ICONS
    def chip(self) -> dict:
        return {
                'bgcolor': colors.BLUE_GREY_800 if self.mode == ThemeMode.DARK else colors.GREY_50,
                'selected_color': colors.DEEP_PURPLE_ACCENT_700
                if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
                'show_checkmark': False
        }

    def switch(self) -> dict:
        return {
            'active_color': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700
        }

    def slider(self) -> dict:
        return {
            'expand': True,
            'min': 8,
            'max': 60,
            'active_color': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700
        }

    @staticmethod
    def icon_copy() -> dict:
        return {
            'icon': icons.COPY,
            'icon_size': 30,
            'offset': Offset(-0.3, 0.1)
        }

    def dark_theme_icon(self) -> dict:
        return {
            'icon_size': 30,
            'selected': True if self.mode == ThemeMode.DARK else False,
            'icon': icons.DARK_MODE if self.mode == ThemeMode.DARK else icons.DARK_MODE_OUTLINED,
            'icon_color': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.BLACK
        }

    def light_theme_icon(self) -> dict:
        return {
            'icon_size': 30,
            'selected': True if self.mode == ThemeMode.LIGHT else False,
            'icon': icons.LIGHT_MODE if self.mode == ThemeMode.LIGHT else icons.LIGHT_MODE_OUTLINED,
            'icon_color': colors.GREY_50 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700
        }

    def icon(self) -> dict:
        return {
            'size': 40,
            'color': colors.WHITE if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700
        }

    @staticmethod
    def website_image() -> dict:
        return {
            'src': '/icons/icon0.png',
            'width': 40,
            'height': 45,
            'border_radius': 5,
            'offset': Offset(0, -0.03)
        }

    def generate_pass_icon(self) -> dict:
        return {
            'icon': icons.LOCK_RESET,
            'icon_size': 40,
            'icon_color': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
            'offset': Offset(0, -0.2)
        }

    # PASSWORD CARD
    def passwords_card(self) -> dict:
        return {
            'shadow_color': colors.WHITE if self.mode == ThemeMode.DARK else colors.BLACK12,
            'elevation': 15,
            'variant': CardVariant.OUTLINED,
            'margin': margin.only(left=20, right=20, top=10)
        }

    def password_tile(self) -> dict:
        return {
            'bgcolor': colors.GREY_900 if self.mode == ThemeMode.DARK else colors.GREY_50,
            'height': 50,
            'shadow': BoxShadow(color=colors.GREY, blur_radius=1.1),
            'animate': animation.Animation(700, AnimationCurve.EASE_IN_OUT),
            'border_radius': 15,
            'margin': margin.only(left=15, right=15, top=10),
        }

    # DROPDOWN / POP_UP / EXPANSION
    def dropdown(self) -> dict:
        return {
            'bgcolor': '#1d1b1f' if self.mode == ThemeMode.DARK else colors.WHITE,
            'border_color': colors.BLACK87,
            'border': 2,
            'border_radius': 10,
            'color': colors.WHITE if self.mode == ThemeMode.DARK else colors.BLACK87,
            'height': 50,
            'expand': True,
            'content_padding': padding.only(bottom=5, left=10),
            'text_style': TextStyle(size=20)
        }

    def pop_up_menu(self) -> dict:
        return {
            'bgcolor': '#1d1b1f' if self.mode == ThemeMode.DARK else colors.WHITE,
            'icon': icons.ARROW_DROP_DOWN,
            'right': 0,
            'offset': Offset(0, 0.09),
        }

    def expansion_panel(self) -> dict:
        return {
            'expand_icon_color': colors.DEEP_PURPLE_ACCENT_700
            if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
            'elevation': 8,
            'divider_color': colors.DEEP_PURPLE_ACCENT_700 if self.mode == ThemeMode.DARK else colors.INDIGO_ACCENT_700,
        }

    # APPBAR
    def appbar(self) -> dict:
        return {
            'toolbar_height': 10,
            'bgcolor': colors.BLACK87 if self.mode == ThemeMode.DARK else colors.WHITE,
        }

    def bottom_appbar(self) -> dict:
        return {
            'shape': NotchShape.AUTO,
            'bgcolor': colors.BLACK if self.mode == ThemeMode.DARK else colors.WHITE,
            'height': 55,
            'padding': padding.only(10, 10, 10, 0),
        }

    def home_icon(self, e):
        if e:
            if self.mode == ThemeMode.DARK:
                return {
                    'selected': True,
                    'icon_color': colors.DEEP_PURPLE_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.HOME
                }
            else:
                return {
                    'selected': True,
                    'icon_color': colors.INDIGO_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.HOME
                }
        else:
            return {
                'selected': False,
                'icon_color': colors.GREY,
                'icon_size': 30,
                'icon': icons.HOME
            }

    def update_icon(self, e):
        if e:
            if self.mode == ThemeMode.DARK:
                return {
                    'selected': True,
                    'icon_color': colors.DEEP_PURPLE_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.UPDATE
                }
            else:
                return {
                    'selected': True,
                    'icon_color': colors.INDIGO_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.UPDATE
                }
        else:
            return {
                'selected': False,
                'icon_color': colors.GREY,
                'icon_size': 30,
                'icon': icons.UPDATE
            }

    def delete_icon(self, e):
        if e:
            if self.mode == ThemeMode.DARK:
                return {
                    'selected': True,
                    'icon_color': colors.DEEP_PURPLE_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.DELETE
                }
            else:
                return {
                    'selected': True,
                    'icon_color': colors.INDIGO_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.DELETE
                }
        else:
            return {
                'selected': False,
                'icon_color': colors.GREY,
                'icon_size': 30,
                'icon': icons.DELETE
            }

    def settings_icon(self, e):
        if e:
            if self.mode == ThemeMode.DARK:
                return {
                    'selected': True,
                    'icon_color': colors.DEEP_PURPLE_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.SETTINGS
                }
            else:
                return {
                    'selected': True,
                    'icon_color': colors.INDIGO_ACCENT_700,
                    'icon_size': 30,
                    'icon': icons.SETTINGS
                }
        else:
            return {
                'selected': False,
                'icon_color': colors.GREY,
                'icon_size': 30,
                'icon': icons.SETTINGS
            }
