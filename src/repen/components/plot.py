from typing import Any

from repen.components.base import Component


class PlotComponent(Component):
    def __init__(self, image_data: Any, format: str = "svg", **metadata) -> None:
        super().__init__(image_data, **metadata)
        self.image_data = image_data
        self.format = format
