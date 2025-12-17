from abc import ABC
from typing import Any


class Component(ABC):
    """
    Abstract base class for report components.

    Components are the building blocks of reports, created automatically by
    ComponentRegistry through registered adapters. Each component holds:
    - data: The actual content to display
    - metadata: Display properties and configuration

    Attributes:
        data: The component's content data.
        metadata: Display properties and configuration.
    """

    def __init__(self, data: Any, **metadata: Any) -> None:
        """
        Initialize a component with data and optional metadata.

        Args:
            data: The content data for this component.
            **metadata: Display properties (title, style, size, etc.).
        """

        self.data = data
        self.metadata = metadata
