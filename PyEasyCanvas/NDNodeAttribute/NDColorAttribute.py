from typing import ForwardRef

from qtpy.QtGui import QColor

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


# noinspection PyPep8Naming
class NDColorAttribute(NDAttributeBase):
    def __init__(self, parentNode: NDNodeBase = None):
        super().__init__(parentNode)
        self._value: QColor = QColor()

    def Type(self) -> int:
        return AttributeTypes.t_color
