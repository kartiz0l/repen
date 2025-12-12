from __future__ import annotations

from pathlib import Path
from typing import Any, List, Union

from repen.component import Component
from repen.renderer import create_renderer


class Report:
    def __init__(self, title: str = "") -> None:
        self._title: str = title
        self._components: List[Component] = []

    def add(self, *items: Any) -> Report:
        for item in items:
            self._components.append(item)
        return self

    def render(self, format: str) -> Union[str, bytes]:
        renderer = create_renderer(format)
        return renderer.render(self._title, self._components)

    def save(self, filepath: Union[str, Path]) -> None:
        path = Path(filepath)
        ext = path.suffix.lower()
        content = self.render(ext)

        if isinstance(content, str):
            path.write_text(content, encoding="utf-8")
        else:
            path.write_bytes(content)
