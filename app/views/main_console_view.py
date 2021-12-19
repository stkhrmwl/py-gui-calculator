import PySimpleGUI as sg

from views.components.button import Button
from views.components.text import Text
from views.styles.base_style import *
from views.styles.button_style import *
from views.styles.text_style import *

from configs.yaml_entry_point import YamlEntryPoint


class MainConsoleView():
    def __init__(self) -> None:

        keys = YamlEntryPoint().ui_keys
        nums = keys['nums']

        layout = [
            [
                Text('0', key=keys['expression'], style=display_style).widget,
            ], [
                Button('7',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('8',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('9',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('/', key=keys['div'], style=op_button_style).widget,
            ], [
                Button('4',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('5',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('6',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('*', key=keys['mul'], style=op_button_style).widget,
            ], [
                Button('1',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('2',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('3',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('-', key=keys['sub'], style=op_button_style).widget,
            ], [
                Button('0',
                       key=keys['number'].format(nums.pop(0)), style=num_button_style).widget,
                Button('C', key=keys['clear'], style=c_button_style).widget,
                Button('=', key=keys['equal'], style=op_button_style).widget,
                Button('+', key=keys['add'], style=op_button_style).widget,
            ],
        ]

        self._window = sg.Window('電卓', layout, **window_style)

    @property
    def window(self):
        return self._window

    def popup_error(self, text=''):
        sg.popup_error(text)
