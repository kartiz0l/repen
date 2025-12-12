from typing import List, Tuple, Union

from repen.component import Component
from repen.renderer.base import Renderer


class HTMLRenderer(Renderer):
    formats: Tuple[str, ...] = ("html", "htm")

    def __init__(self) -> None:
        super().__init__()
        self._parts: List[str] = []

    def begin(self, title: str = "") -> None:
        self._parts.append(
            f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
        """
        )

    def component(self, component: Component) -> None:
        pass

    def end(self) -> Union[str, bytes]:
        self._parts.append(
            f"""
        </body>
        </html>
        """
        )
        return "".join(self._parts)
