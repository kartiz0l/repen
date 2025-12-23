from typing import Dict, List, Type, Union

from repen.components import (Component, Composite, Text, TextBlock, TextLines,
                              TextSpan)
from repen.renderers.base import Renderer
from repen.renderers.html.processor import (HTMLComponentProcessor,
                                            HTMLCompositeProcessor)
from repen.renderers.html.processor_text import (HTMLTextBlockProcessor,
                                                 HTMLTextLinesProcessor,
                                                 HTMLTextProcessor,
                                                 HTMLTextSpanProcessor)


class HTMLRenderer(Renderer):
    def __init__(self, **metadata) -> None:
        super().__init__(**metadata)
        self._output: List[str] = []
        self._component_processors: Dict[Type, HTMLComponentProcessor] = {
            Text: HTMLTextProcessor(),
        }
        self._composite_processors: Dict[Type, HTMLCompositeProcessor] = {
            TextBlock: HTMLTextBlockProcessor(),
            TextSpan: HTMLTextSpanProcessor(),
            TextLines: HTMLTextLinesProcessor(),
        }

    def render(self, title: str, root: Component) -> Union[str, bytes]:
        self.begin(title)
        self.component(root)
        self.end()
        return self.output()

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

    def component(self, component: Component) -> None:
        if isinstance(component, Composite):
            processor = self._composite_processors.get(
                type(component),
                HTMLCompositeProcessor(),
            )
            composite_begin = processor.begin(component)
            if composite_begin is not None:
                self._output.append(composite_begin)

            for child in component.children:
                composite_begin_component = processor.begin_component(component, child)
                if composite_begin_component is not None:
                    self._output.append(composite_begin_component)

                self.component(child)

                composite_end_component = processor.end_component(component, child)
                if composite_end_component is not None:
                    self._output.append(composite_end_component)

            composite_end = processor.end(component)
            if composite_end is not None:
                self._output.append(composite_end)
        else:
            processor = self._component_processors.get(
                type(component),
                HTMLComponentProcessor(),
            )
            component_processed = processor.process(component)
            if component_processed:
                self._output.append(component_processed)

    def output(self) -> Union[str, bytes]:
        return "".join(self._output)
