from typing import Any, ClassVar, List, Type

from repen.adapters.base import ComponentAdapter
from repen.components.base import Component
from repen.components.generic import GenericComponent


class ComponentRegistry:
    """
    Registry for component adapters that can create Component instances from various data sources.

    This class implements a registry pattern with adapter support, allowing flexible
    component creation from different data formats. When no suitable adapter is found,
    it falls back to creating a GenericComponent.

    Attributes:
        _adapters: Class variable storing all registered adapters.

    Methods:
        register: Register a new adapter.
        unregister: Remove an adapter by its type.
        create: Create a component from data using registered adapters.
        clear: Remove all registered adapters.
    """

    _adapters: ClassVar[List[ComponentAdapter]] = []

    @classmethod
    def register(cls, adapter: ComponentAdapter) -> None:
        """
        Register a new component adapter.

        Args:
            adapter: The adapter instance to register.

        Example:
            >>> class JSONAdapter(ComponentAdapter):
            ...     def can_adapt(self, data, **metadata):
            ...         return isinstance(data, str) and data.startswith('{')
            ...
            ...     def adapt(self, data, **metadata):
            ...         import json
            ...         return JSONComponent(json.loads(data), **metadata)
            >>>
            >>> ComponentRegistry.register(JSONAdapter())
        """

        cls._adapters.append(adapter)

    @classmethod
    def unregister(cls, adapter_type: Type[ComponentAdapter]) -> None:
        """
        Unregister all adapters of the specified type.

        Args:
            adapter_type: The type of adapter to remove.

        Example:
            >>> ComponentRegistry.unregister(JSONAdapter)
        """

        cls._adapters = [
            adapter
            for adapter in cls._adapters
            if not isinstance(adapter, adapter_type)
        ]

    @classmethod
    def create(cls, data: Any, **metadata: Any) -> Component:
        """
        Create a Component instance from data using registered adapters.

        This method iterates through all registered adapters in registration order
        and uses the first adapter that can handle the data. If no adapter can handle
        the data, it falls back to creating a GenericComponent.

        Args:
            data: The data to adapt into a Component.
            **metadata: Additional metadata to pass to the component constructor.

        Returns:
            A Component instance created from the data.

        Raises:
            ValueError: If no adapter can handle the data and fallback creation fails.

        Example:
            >>> data = {'header': ['#1', '#2'], 'rows': [['A', 1], ['B', 2]]}
            >>> component = ComponentRegistry.create(data, title='My Table')
            >>> isinstance(component, DataTableComponent)
            True
        """
        for adapter in cls._adapters:
            if adapter.can_adapt(data, **metadata):
                try:
                    return adapter.adapt(data, **metadata)
                except:
                    # Skip any fails
                    continue

        # Fallback to GenericComponent
        try:
            return GenericComponent(data, **metadata)
        except Exception as e:
            raise ValueError(
                f"Failed to create component from data. No suitable adapter found "
                f"and GenericComponent creation failed: {str(e)}"
            ) from e

    @classmethod
    def clear(cls) -> None:
        """Clear all registered adapters."""

        cls._adapters.clear()
