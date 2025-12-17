from typing import Iterable, List

from repen.components.base import Component
from repen.layouts.base import Layout


class VerticalLayout(Layout):
    def arrange(self, components: List[Component]) -> Iterable[Component]:
        return components
