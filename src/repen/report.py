from __future__ import annotations

from pathlib import Path
from typing import Any, List, Union

from repen.adapters import AdapterRegistry
from repen.components import Component, Layout, VStack
from repen.renderers import DebugRenderer, HTMLRenderer, Renderer


class Report:
    def __init__(self, **metadata) -> None:
        self._title: str = metadata.pop("title", "")
        self._components: List[Component] = []
        self._layout: Layout = metadata.pop("layout", VStack(**metadata))
        self._renderer: Renderer = metadata.pop("renderer", HTMLRenderer(**metadata))
        self._debug: bool = metadata.pop("debug", False)

    def add(self, item: Any, **metadata) -> Report:
        self._components.append(AdapterRegistry.create(item, **metadata))
        return self

    def render(self) -> Union[str, bytes]:
        if len(self._components) == 0:
            raise ValueError("No any data added into report.")

        layout = self._layout.__class__(**self._layout.metadata)
        layout.add_all(*self._components)

        if self._debug:
            debug_renderer = DebugRenderer()
            print(debug_renderer.render(self._title, layout))

        return self._renderer.render(self._title, layout)

    def save(self, filepath: Union[str, Path]) -> None:
        path = Path(filepath)
        content = self.render()

        if isinstance(content, str):
            path.write_text(content, encoding="utf-8")
        else:
            path.write_bytes(content)
