from typing import Any, ClassVar, List, Type

from repen.adapters.base import ComponentAdapter
from repen.components import Component, Generic


class AdapterRegistry:
    _adapters: ClassVar[List[ComponentAdapter]] = []

    @classmethod
    def register(cls, adapter: ComponentAdapter) -> None:
        cls._adapters.append(adapter)

    @classmethod
    def unregister(cls, adapter_type: Type[ComponentAdapter]) -> None:
        cls._adapters = [
            adapter
            for adapter in cls._adapters
            if not isinstance(adapter, adapter_type)
        ]

    @classmethod
    def create(cls, raw_data: Any, **metadata: Any) -> Component:
        for adapter in cls._adapters:
            if adapter.can_adapt(raw_data, **metadata):
                try:
                    return adapter.adapt(raw_data, **metadata)
                except:
                    # Skip any fails
                    continue

        # Fallback to GenericComponent
        try:
            return Generic(raw_data, **metadata)
        except Exception as e:
            raise ValueError(
                f"Failed to create component from raw data. No suitable adapter found "
                f"and GenericComponent creation failed: {str(e)}"
            ) from e

    @classmethod
    def clear(cls) -> None:
        cls._adapters.clear()
