from controllers.view_controllers.main_console_controller import MainConsoleController


class MainController():
    def __init__(self) -> None:
        self._main_console_ctrl = MainConsoleController()

    def run(self) -> None:
        self._main_console_ctrl.show()
