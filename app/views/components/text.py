import PySimpleGUI as sg


class Text():
    def __init__(self, title='', key=None, style=None) -> None:
        self._widget = sg.Text(title, key=key, **style)

    @property
    def widget(self):
        return self._widget
