from __future__ import annotations

from pathlib import Path
from typing import Any, List, Union

from repen.components.base import Component
from repen.layouts.base import Layout
from repen.layouts.vertical import VerticalLayout
from repen.registry import ComponentRegistry
from repen.renderers.base import Renderer
from repen.renderers.html.renderer import HTMLRenderer


class Report:
    def __init__(self, **metadata) -> None:
        self._title: str = metadata.pop("title", "")
        self._components: List[Component] = []
        self._layout: Layout = metadata.pop("layout", VerticalLayout(**metadata))
        self._renderer: Renderer = metadata.pop("renderer", HTMLRenderer(**metadata))

    def add(self, item: Any, **metadata) -> Report:
        self._components.append(ComponentRegistry.create(item, **metadata))
        return self

    def render(self) -> Union[str, bytes]:
        return self._renderer.render(self._title, self._layout, self._components)

    def save(self, filepath: Union[str, Path]) -> None:
        path = Path(filepath)
        content = self.render()

        if isinstance(content, str):
            path.write_text(content, encoding="utf-8")
        else:
            path.write_bytes(content)
