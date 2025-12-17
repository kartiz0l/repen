from repen.components.base import Component


class TextComponent(Component):
    def __init__(self, content: str, **metadata) -> None:
        super().__init__(content, **metadata)
        self.content = content
