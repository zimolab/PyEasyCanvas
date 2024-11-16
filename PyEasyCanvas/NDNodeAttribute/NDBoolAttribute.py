from typing import ForwardRef

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


# noinspection PyPep8Naming
class NDBoolAttribute(NDAttributeBase):
    def __init__(self, parentNode: NDNodeBase = None):
        super().__init__(parentNode)
        self._value = True

    def Type(self) -> int:
        return AttributeTypes.t_bool
