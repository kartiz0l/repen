from typing import Any

from repen.components.base import Component


class GenericComponent(Component):
    def __init__(self, data: Any, **metadata) -> None:
        super().__init__(data, **metadata)

    def __repr__(self) -> str:
        str_data = str(self.data)
        return f"{self.__class__.__name__}: {str_data[:min(50, len(str_data))]}..."
