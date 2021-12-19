import PySimpleGUI as sg


class Button():
    def __init__(self, title='', key=None, style=None) -> None:
        self._widget = sg.Button(title, key=key, **style)

    @property
    def widget(self):
        return self._widget
