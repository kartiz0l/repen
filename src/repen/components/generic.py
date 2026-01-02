from typing import Any, cast

from repen.components.base import Component


class Generic(Component):
    def __init__(self, raw_data: Any, **metadata: Any) -> None:
        super().__init__(**metadata)
        self._raw_data = raw_data

    def copy(self) -> Component:
        new_instance: Generic = cast(Generic, super().copy())
        new_instance._raw_data = self._raw_data
        return new_instance

    def __repr__(self) -> str:
        raw_data = str(self._raw_data)
        raw_data_preview = raw_data[: min(30, len(raw_data))]
        return f"{self.__class__.__name__} (raw='{raw_data_preview}{'...' if len(raw_data) > 30 else ''}')"
