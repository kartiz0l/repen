from abc import ABC, abstractmethod
from typing import Iterable, List

from repen.components.base import Component


class Layout(ABC):
    """
    Abstract base class for component layouts.

    Layouts control the spatial arrangement of components in a report.
    Different layouts implement different organization strategies (grid, flow, etc.).

    Attributes:
        metadata: Layout configuration options.
    """

    def __init__(self, **metadata) -> None:
        """
        Initialize a layout with optional metadata.

        Args:
            **metadata: Layout configuration (spacing, alignment, etc.).
        """

        self.metadata = metadata

    @abstractmethod
    def arrange(self, components: List[Component]) -> Iterable[Component]:
        """
        Arrange components according to the layout strategy.

        Args:
            components: List of components to arrange.

        Returns:
            Components in the order they should be rendered.

        Note:
            This method may reorder, filter, or group components based on
            the layout's organization strategy.
        """
        pass
