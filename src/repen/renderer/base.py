from abc import ABC, abstractmethod
from typing import List, Tuple, Union

from repen.component import Component


class Renderer(ABC):
    """Abstract base class for report rendering to various output formats.

    Provides a streaming API for incrementally building formatted reports
    from components, with format-specific rendering implementations.
    """

    #: Tuple of file format extensions supported by this renderer
    #: (e.g., ('html', 'htm') for HTML renderer, ('pdf') for PDF renderer)
    formats: Tuple[str, ...] = ()

    @abstractmethod
    def begin(self, title: str = "") -> None:
        pass

    @abstractmethod
    def component(self, component: Component) -> None:
        pass

    @abstractmethod
    def end(self) -> Union[str, bytes]:
        pass

    def render(self, title: str, components: List[Component]) -> Union[str, bytes]:
        self.begin(title)
        return self.end()

    @classmethod
    def supports(cls, format: str) -> bool:
        return format in cls.formats
