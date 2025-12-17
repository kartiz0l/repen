from typing import Any

from repen.adapters.base import ComponentAdapter
from repen.components.base import Component
from repen.components.text import TextComponent


class TextComponentAdapter(ComponentAdapter):
    def can_adapt(self, data: Any, **metadata: Any) -> bool:
        return isinstance(data, str)

    def adapt(self, data: Any, **metadata: Any) -> Component:
        content = str(data)
        return TextComponent(content, **metadata)
