from enum import Enum
from typing import Optional, cast

from repen.components.base import Component, Composite


class Spacing(Enum):
    NONE = "0"
    XS = "xs"
    SM = "sm"
    MD = "md"
    LG = "lg"
    XL = "xl"
    XXL = "2xl"


class Layout(Composite):
    pass


class VStack(Layout):
    def __init__(self, spacing: Spacing = Spacing.NONE, **metadata) -> None:
        super().__init__(**metadata)
        self.spacing = spacing

    def copy(self) -> Component:
        new_instance = cast(VStack, super().copy())
        new_instance.spacing = self.spacing
        return new_instance

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (spacing={self.spacing})"


class HStack(Layout):
    def __init__(self, spacing: Spacing = Spacing.NONE, **metadata) -> None:
        super().__init__(**metadata)
        self.spacing = spacing

    def copy(self) -> Component:
        new_instance = cast(HStack, super().copy())
        new_instance.spacing = self.spacing
        return new_instance

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (spacing={self.spacing})"
