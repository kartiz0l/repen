from abc import ABC, abstractmethod

from repen.components.base import Component
from repen.layouts.base import Layout


class HTMLLayoutProcessor(ABC):
    @abstractmethod
    def begin(self, layout: Layout) -> str:
        pass

    @abstractmethod
    def end(self, layout: Layout) -> str:
        pass

    @abstractmethod
    def begin_component(self, layout: Layout, component: Component) -> str:
        pass

    @abstractmethod
    def end_component(self, layout: Layout, component: Component) -> str:
        pass


class HTMLComponentProcessor(ABC):
    @abstractmethod
    def process(self, component: Component) -> str:
        pass
