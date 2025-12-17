from repen.components.base import Component
from repen.layouts.base import Layout
from repen.renderers.html.processor import HTMLLayoutProcessor


class HTMLVerticalLayoutProcessor(HTMLLayoutProcessor):
    def begin(self, layout: Layout) -> str:
        return f"<div class='layout vertical'>"

    def end(self, layout: Layout) -> str:
        return "</div>"

    def begin_component(self, layout: Layout, component: Component) -> str:
        return f"<div class='item'>"

    def end_component(self, layout: Layout, component: Component) -> str:
        return "</div>"
