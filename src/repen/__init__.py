from repen.adapters import (ComponentAdapter, MatplotlibPlotComponentAdapter,
                            TextComponentAdapter)
from repen.layouts import Layout, VerticalLayout
from repen.registry import ComponentRegistry
from repen.renderers import HTMLRenderer, Renderer
from repen.report import Report

# Register default adapters
ComponentRegistry.register(TextComponentAdapter())

# Matplotlib
try:
    import matplotlib

    ComponentRegistry.register(MatplotlibPlotComponentAdapter())
except:
    pass

__all__ = [
    "Report",
    "ComponentRegistry",
    "ComponentAdapter",
    "TextComponentAdapter",
    "MatplotlibPlotComponentAdapter",
    "Layout",
    "VerticalLayout",
    "HTMLRenderer",
    "Renderer",
]
