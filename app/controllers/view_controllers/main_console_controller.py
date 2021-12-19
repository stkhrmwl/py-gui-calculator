from views.main_console_view import MainConsoleView
from models.calculator import Calculator

from configs.yaml_entry_point import YamlEntryPoint


class MainConsoleController():
    def __init__(self) -> None:
        self._main_console_view = MainConsoleView()
        self._calc = Calculator()
        self._ui_keys = YamlEntryPoint().ui_keys
        nums = self._ui_keys['nums']
        self._func_dict = {
            self._ui_keys['add']: self._push_op,
            self._ui_keys['sub']: self._push_op,
            self._ui_keys['mul']: self._push_op,
            self._ui_keys['div']: self._push_op,
            self._ui_keys['equal']: self._equal,
            self._ui_keys['clear']: self._clear,
        }
        self._func_dict.update({
            self._ui_keys['number'].format(num): self._push_num for num in nums
        })

    def show(self) -> None:
        while True:
            event, values = self._main_console_view.window.read()

            self._handle_event(event, values)

            if event is None:
                print('Quit')
                break

        self._main_console_view.window.close()

    def _handle_event(self, event_key, values) -> None:
        if event_key not in self._func_dict:
            return
        event_func = self._func_dict[event_key]
        event_func(event_key, values)

    def _push_num(self, event_key, _) -> None:
        num = int(self._main_console_view.window[event_key].get_text())
        if self._calc.push_num(num):
            self._update_expression()
        else:
            self._popup_error()

    def _push_op(self, event_key, _) -> None:
        op = self._main_console_view.window[event_key].get_text()
        if self._calc.push_op(op):
            self._update_expression()
        else:
            self._popup_error()

    def _equal(self, *_) -> None:
        if self._calc.calc():
            self._update_expression()
        else:
            self._popup_error()

    def _clear(self, *_) -> None:
        self._calc.clear()
        self._update_expression()

    def _update_expression(self) -> None:
        self._main_console_view.window[self._ui_keys['expression']].update(
            self._calc.expression())

    def _popup_error(self, text='') -> None:
        self._main_console_view.popup_error(
            text if text != '' else '不正な入力です')
