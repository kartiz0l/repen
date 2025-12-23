from __future__ import annotations

from abc import ABC
from typing import Any, List, Tuple, final


class Component(ABC):
    def __init__(self, **metadata: Any) -> None:
        self.metadata = metadata

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ()"


class Composite(Component):
    def __init__(self, **metadata: Any) -> None:
        super().__init__(**metadata)
        self._children: List[Component] = []

    def add(self, component: Component) -> Composite:
        self._children.append(component)
        return self

    def add_all(self, *components: Component) -> Composite:
        for component in components:
            self.add(component)
        return self

    def remove(self, component: Component) -> None:
        if component in self._children:
            self._children.remove(component)
        else:
            for child_component in self._children:
                if isinstance(child_component, Composite):
                    child_component.remove(component)

    @property
    @final
    def children(self) -> Tuple[Component, ...]:
        return tuple(self._children)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ()"
