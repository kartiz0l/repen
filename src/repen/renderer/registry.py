from typing import Dict, Type

from repen.renderer.base import Renderer


class Registry:
    _renderers: Dict[str, Type[Renderer]] = {}

    @classmethod
    def register(cls, renderer_class: Type[Renderer]) -> None:
        for format in renderer_class.formats:
            cls._renderers[format] = renderer_class

    @classmethod
    def create(cls, format_or_path: str) -> Renderer:
        # Determine format
        if "." in format_or_path and "/" not in format_or_path:
            format = format_or_path.lstrip(".")
        elif "." in format_or_path:
            from pathlib import Path

            format = Path(format_or_path).suffix.lstrip(".")
        else:
            format = format_or_path

        # Try to create Renderer
        format = format.lower()
        if format not in cls._renderers:
            raise ValueError(
                f"No renderer registered for format: '{format}'. "
                f"Available formats: {list(cls._renderers.keys())}"
            )
        renderer_class = cls._renderers[format]
        return renderer_class()
