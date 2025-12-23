from repen.components.base import Composite


class Layout(Composite):
    pass


class VStack(Layout):
    def __init__(self, spacing: int = 0, **metadata) -> None:
        super().__init__(**metadata)
        self.spacing = spacing

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (spacing={self.spacing})"


class HStack(Layout):
    def __init__(self, spacing: int = 0, **metadata) -> None:
        super().__init__(**metadata)
        self.spacing = spacing

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (spacing={self.spacing})"
