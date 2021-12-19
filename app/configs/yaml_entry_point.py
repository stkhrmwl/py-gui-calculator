import yaml


class YamlEntryPoint():
    def __init__(self) -> None:
        with open('app/configs/ui_keys.yml', 'r') as ui_keys:
            self._ui_keys = yaml.safe_load(ui_keys)

    @property
    def ui_keys(self):
        return self._ui_keys
