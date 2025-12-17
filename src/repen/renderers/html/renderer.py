from typing import Dict, List, Type, Union

from repen.components.base import Component
from repen.components.plot import PlotComponent
from repen.components.text import TextComponent
from repen.layouts.base import Layout
from repen.layouts.vertical import VerticalLayout
from repen.renderers.base import Renderer
from repen.renderers.html.processor import (HTMLComponentProcessor,
                                            HTMLLayoutProcessor)
from repen.renderers.html.processor_generic import (
    HTMLGenericComponentProcessor, HTMLGenericLayoutProcessor)
from repen.renderers.html.processor_plot import HTMLPlotComponentProcessor
from repen.renderers.html.processor_text import HTMLTextComponentProcessor
from repen.renderers.html.processor_vertical import HTMLVerticalLayoutProcessor


class HTMLRenderer(Renderer):
    def __init__(self, **metadata) -> None:
        super().__init__(**metadata)
        self._output: List[str] = []
        self._layout_processors: Dict[Type, HTMLLayoutProcessor] = {}
        self._component_processors: Dict[Type, HTMLComponentProcessor] = {}

        self._register_default_processors()

    def begin(self, title: str = "") -> None:
        self._output.append(
            f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
"""
        )

    def end(self) -> None:
        self._output.append(
            """</body>
</html>
"""
        )

    def begin_layout(self, layout: Layout) -> None:
        processor = self._get_layout_processor(layout)
        self._output.append(processor.begin(layout))

    def end_layout(self, layout: Layout) -> None:
        processor = self._get_layout_processor(layout)
        self._output.append(processor.end(layout))

    def begin_layout_component(self, layout: Layout, component: Component) -> None:
        processor = self._get_layout_processor(layout)
        self._output.append(processor.begin_component(layout, component))

    def end_layout_component(self, layout: Layout, component: Component) -> None:
        processor = self._get_layout_processor(layout)
        self._output.append(processor.end_component(layout, component))

    def component(self, component: Component) -> None:
        processor = self._get_component_processor(component)
        self._output.append(processor.process(component))

    def output(self) -> Union[str, bytes]:
        return "".join(self._output)

    def register_layout_processor(
        self,
        layout_type: Type[Layout],
        processor: HTMLLayoutProcessor,
    ) -> None:
        if layout_type in self._layout_processors:
            raise ValueError(
                f"Processor for layout '{layout_type}' with name '{processor.__name__}' already registered."
            )
        self._layout_processors[layout_type] = processor

    def register_component_processor(
        self,
        component_type: Type[Component],
        processor: HTMLComponentProcessor,
    ) -> None:
        if component_type in self._component_processors:
            raise ValueError(
                f"Processor for component '{component_type}' with name '{processor.__name__}' already registered."
            )
        self._component_processors[component_type] = processor

    def _register_default_processors(self) -> None:
        # Layouts
        self.register_layout_processor(VerticalLayout, HTMLVerticalLayoutProcessor())

        # Components
        self.register_component_processor(TextComponent, HTMLTextComponentProcessor())
        self.register_component_processor(PlotComponent, HTMLPlotComponentProcessor())

    def _get_layout_processor(self, layout: Layout) -> HTMLLayoutProcessor:
        layout_type = type(layout)
        return self._layout_processors.get(layout_type, HTMLGenericLayoutProcessor())

    def _get_component_processor(self, component: Component) -> HTMLComponentProcessor:
        component_type = type(component)
        return self._component_processors.get(
            component_type, HTMLGenericComponentProcessor()
        )
