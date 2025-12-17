from typing import cast

from repen.components.base import Component
from repen.components.text import TextComponent
from repen.renderers.html.processor import HTMLComponentProcessor


class HTMLTextComponentProcessor(HTMLComponentProcessor):
    def process(self, component: Component) -> str:
        text_component: TextComponent = cast(TextComponent, component)
        content = text_component.content
        return f"<p class='component text'>{content}</p>"
