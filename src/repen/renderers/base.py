from abc import ABC, abstractmethod
from typing import List, Union

from repen.components.base import Component
from repen.layouts.base import Layout


class Renderer(ABC):
    """
    Abstract base class for rendering reports from layouts and components.

    This class implements the Template Method pattern, providing a fixed rendering
    pipeline with customizable steps. Subclasses implement specific rendering logic
    for different output formats (HTML, PDF, Markdown, etc.).

    The rendering process follows this sequence:
    1. begin() - Initialize rendering
    2. begin_layout() - Start layout rendering
    3. For each component in layout.arrange():
        a. begin_layout_component() - Start component container
        b. component() - Render the component content
        c. end_layout_component() - End component container
    4. end_layout() - End layout rendering
    5. end() - Finalize rendering
    6. output() - Get final result

    Attributes:
        metadata: Additional rendering options passed to the constructor.

    Methods:
        render: Main entry point for rendering a complete report.
        begin: Initialize the rendering process.
        end: Finalize the rendering process.
        begin_layout: Start rendering a layout.
        end_layout: End rendering a layout.
        begin_layout_component: Start rendering a component within a layout.
        end_layout_component: End rendering a component within a layout.
        component: Render a single component.
        output: Get the final rendered output.
    """

    def __init__(self, **metadata) -> None:
        """
        Initialize the renderer with optional metadata.

        Args:
            **metadata: Additional rendering options (theme, format, etc.).
                        These are stored in self.metadata for use by subclasses.
        """

        self.metadata = metadata

    def render(
        self,
        title: str,
        layout: Layout,
        components: List[Component],
    ) -> Union[str, bytes]:
        """
        Render a complete report with title, layout, and components.

        This is the main entry point that orchestrates the entire rendering process.
        It follows the Template Method pattern, calling abstract methods in a
        specific order to produce the final output.

        Args:
            title: Report title to display.
            layout: Layout manager for arranging components.
            components: List of components to render.

        Returns:
            The rendered output as string (HTML, Markdown) or bytes (PDF, image).

        Example:
            >>> report = renderer.render(
            ...     title="Sales Dashboard",
            ...     layout=VerticalLayout(),
            ...     components=[
            ...         SalesChart(),
            ...         RevenueTable(),
            ...         KPIWidgets()
            ...     ]
            ... )
            >>> isinstance(report, str)  # or bytes for binary formats
            True
        """

        self.begin(title)
        self.begin_layout(layout)
        for component in layout.arrange(components):
            self.begin_layout_component(layout, component)
            self.component(component)
            self.end_layout_component(layout, component)
        self.end_layout(layout)
        self.end()

        return self.output()

    # Abstract methods - interface for concrete renderers

    @abstractmethod
    def begin(self, title: str = "") -> None:
        """Initialize the rendering process."""
        pass

    @abstractmethod
    def end(self) -> None:
        """Finalize the rendering process."""
        pass

    @abstractmethod
    def begin_layout(self, layout: Layout) -> None:
        """Start rendering a layout container."""
        pass

    @abstractmethod
    def end_layout(self, layout: Layout) -> None:
        """End rendering a layout container."""
        pass

    @abstractmethod
    def begin_layout_component(self, layout: Layout, component: Component) -> None:
        """Start rendering a component within a layout."""
        pass

    @abstractmethod
    def end_layout_component(self, layout: Layout, component: Component) -> None:
        """End rendering a component within a layout."""
        pass

    @abstractmethod
    def component(self, component: Component) -> None:
        """Render a single component's content."""
        pass

    @abstractmethod
    def output(self) -> Union[str, bytes]:
        """Get the final rendered output."""
        pass
