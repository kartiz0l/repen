from typing import cast

from repen.components.base import Component
from repen.components.generic import GenericComponent
from repen.layouts.base import Layout
from repen.renderers.html.processor import (HTMLComponentProcessor,
                                            HTMLLayoutProcessor)


class HTMLGenericLayoutProcessor(HTMLLayoutProcessor):
    def begin(self, layout: Layout) -> str:
        return f"<div class='layout default'>"

    def end(self, layout: Layout) -> str:
        return "</div>"

    def begin_component(self, layout: Layout, component: Component) -> str:
        return f"<div class='item'>"

    def end_component(self, layout: Layout, component: Component) -> str:
        return "</div>"


class HTMLGenericComponentProcessor(HTMLComponentProcessor):
    def process(self, component: Component) -> str:
        generic_component: GenericComponent = cast(GenericComponent, component)
        return f"<div class='component generic'>{generic_component.data}</div>"
