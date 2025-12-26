from repen.adapters.base import ComponentAdapter
from repen.adapters.image import BytesImageAdapter, PathImageAdapter
from repen.adapters.registry import AdapterRegistry
from repen.adapters.text import TextAdapter

# Image
AdapterRegistry.register(PathImageAdapter())
AdapterRegistry.register(BytesImageAdapter())

try:
    import PIL
    from repen.adapters.image import PillowImageAdapter

    AdapterRegistry.register(PillowImageAdapter())
except:
    pass

# Text
AdapterRegistry.register(TextAdapter())

__all__ = [
    "ComponentAdapter",
    "AdapterRegistry",
]
