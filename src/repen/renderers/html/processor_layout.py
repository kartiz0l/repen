from typing import Optional

from repen.components import Component, Composite
from repen.renderers.html.processor import HTMLCompositeProcessor


class HTMLVStackProcessor(HTMLCompositeProcessor):
    def begin(self, composite: Composite) -> Optional[str]:
        return "<div class='layout vstack'>"

    def begin_child(
        self,
        composite: Composite,
        component: Component,
    ) -> Optional[str]:
        return "<div class='item'>"

    def end_child(
        self,
        composite: Composite,
        component: Component,
    ) -> Optional[str]:
        return "</div>"

    def end(self, composite: Composite) -> Optional[str]:
        return "</div>"
