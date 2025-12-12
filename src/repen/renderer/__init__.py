from .base import Renderer
from .html import HTMLRenderer
from .registry import Registry

# Auto-registration of built-in renderers
# Each renderer is automatically registered upon import and becomes
# immediately available through the create_renderer() factory function.
Registry.register(HTMLRenderer)


def create_renderer(format_or_path: str) -> Renderer:
    return Registry.create(format_or_path)


__all__ = [
    "create_renderer",  # Primary factory function for client code
    "Renderer",  # Abstract base class for custom renderer implementations
    # Note: Registry is intentionally not exported as it's an internal component
]
