from abc import ABC, abstractmethod
from typing import Any

from repen.components.base import Component


class ComponentAdapter(ABC):
    """
    Abstract base class for adapting data to Component instances.

    This class defines the interface that all component adapters must implement.
    Adapters are responsible for:
    1. Determining if they can handle a given data format (can_adapt)
    2. Converting data into a Component instance (adapt)

    Adapters are typically registered with ComponentRegistry to enable automatic
    component creation from various data sources.

    Methods:
        can_adapt: Check if this adapter can handle the given data.
        adapt: Convert data into a Component instance.
    """

    @abstractmethod
    def can_adapt(self, data: Any, **metadata: Any) -> bool:
        """
        Determine if this adapter can handle the given data.

        This method should perform a lightweight check to determine if the adapter
        is capable of converting the provided data into a Component. The check
        should be fast and not involve expensive parsing or validation.

        Args:
            data: The data to check for adaptability.
            **metadata: Additional metadata that might influence the decision.

        Returns:
            True if this adapter can convert the data to a Component, False otherwise.

        Example:
            >>> class CSVAdapter(ComponentAdapter):
            ...     def can_adapt(self, data: Any, **metadata) -> bool:
            ...         # Check if it looks like CSV data
            ...         if isinstance(data, str):
            ...             lines = data.strip().split('\\n')
            ...             return len(lines) > 0 and ',' in lines[0]
            ...         return False
        """
        pass

    @abstractmethod
    def adapt(self, data: Any, **metadata: Any) -> Component:
        """
        Convert data into a Component instance.

        This method should perform the actual conversion of data into a Component.
        It is only called if can_adapt() returned True for the same data.

        Args:
            data: The data to convert into a Component.
            **metadata: Additional metadata to pass to the component constructor.

        Returns:
            A Component instance created from the data.

        Example:
            >>> class DictAdapter(ComponentAdapter):
            ...     def can_adapt(self, data: Any, **metadata) -> bool:
            ...         return isinstance(data, dict)
            ...
            ...     def adapt(self, data: Any, **metadata) -> Component:
            ...         if 'type' not in data:
            ...             raise ValueError("Missing 'type' key in data")
            ...         return create_component_from_dict(data, **metadata)

        Note:
            This method should handle any necessary parsing, validation, and
            transformation of the data into the appropriate Component format.
        """
        pass
