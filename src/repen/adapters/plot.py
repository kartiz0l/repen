from typing import Any, cast

from repen.adapters.base import ComponentAdapter
from repen.components.base import Component
from repen.components.plot import PlotComponent


class MatplotlibPlotComponentAdapter(ComponentAdapter):
    def can_adapt(self, data: Any, **metadata: Any) -> bool:
        from matplotlib.figure import Figure

        return isinstance(data, Figure)

    def adapt(self, data: Any, **metadata: Any) -> Component:
        format = metadata.pop("format", "svg")
        if format == "svg":
            image_data = self._to_svg(data, **metadata)
        elif format == "png":
            image_data = self._to_png(data, **metadata)
        else:
            raise ValueError(f"Unsupported format: {format}")

        return PlotComponent(image_data, format, **metadata)

    def _to_svg(self, data: Any, **metadata: Any) -> str:
        import io
        import re

        from matplotlib.figure import Figure

        output = io.StringIO()
        dpi = metadata.get("dpi", 100)
        figure = cast(Figure, data)
        figure.savefig(output, format="svg", dpi=dpi, bbox_inches="tight")

        svg_content = output.getvalue()
        output.close()

        svg_match = re.search(r"<svg.*</svg>", svg_content, re.DOTALL)
        return svg_match.group(0) if svg_match else svg_content

    def _to_png(self, data: Any, **metadata: Any) -> str:
        import base64
        import io

        from matplotlib.figure import Figure

        output = io.BytesIO()
        dpi = metadata.get("dpi", 100)
        figure = cast(Figure, data)
        figure.savefig(output, format="png", dpi=dpi, bbox_inches="tight")
        output.seek(0)

        return base64.b64encode(output.read()).decode()
