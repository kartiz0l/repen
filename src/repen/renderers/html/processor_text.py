from typing import Optional, cast

from repen.components import Component, Composite, Text, TextBlock
from repen.renderers.html.processor import (HTMLComponentProcessor,
                                            HTMLCompositeProcessor)


class HTMLTextProcessor(HTMLComponentProcessor):
    def process(self, component: Component) -> Optional[str]:
        text = cast(Text, component)
        return text.content


class HTMLTextBlockProcessor(HTMLCompositeProcessor):
    def begin(self, composite: Composite) -> Optional[str]:
        text_block = cast(TextBlock, composite)
        return "<p>"

    def end(self, composite: Composite) -> Optional[str]:
        text_block = cast(TextBlock, composite)
        return "</p>"


class HTMLTextSpanProcessor(HTMLCompositeProcessor):
    pass


class HTMLTextLinesProcessor(HTMLCompositeProcessor):
    def end_component(
        self,
        composite: Composite,
        component: Component,
    ) -> Optional[str]:
        return "</br>"
