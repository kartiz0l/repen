from repen.adapters.base import ComponentAdapter
from repen.adapters.registry import AdapterRegistry
from repen.adapters.text import TextAdapter

AdapterRegistry.register(TextAdapter())

__all__ = [
    "ComponentAdapter",
    "AdapterRegistry",
]
