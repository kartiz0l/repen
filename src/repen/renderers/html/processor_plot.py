from typing import cast

from repen.components.base import Component
from repen.components.plot import PlotComponent
from repen.renderers.html.processor import HTMLComponentProcessor


class HTMLPlotComponentProcessor(HTMLComponentProcessor):
    def process(self, component: Component) -> str:
        plot_component: PlotComponent = cast(PlotComponent, component)

        if plot_component.format == "svg":
            return f"<div class='component plot'>{plot_component.image_data}</div>"
        elif plot_component.format == "png":
            return f"<div class='component plot'><img src='data:image/png;base64,{plot_component.image_data}' /></div>"
        else:
            return f"<div class='component plot unknown'>Unsupported plot format: {plot_component.format}</div>"
