from typing import ForwardRef, Optional, Tuple

from qtpy.QtCore import QPoint

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


# noinspection PyPep8Naming
class NDPosition2DAttribute(NDAttributeBase):
    def __init__(self, parentNode: Optional[NDNodeBase] = None):
        super().__init__(parentNode)
        self._value = QPoint(0, 0)

    def setCurrentValue(self, value: QPoint):
        needSendSignal = True
        if self._value == value:
            needSendSignal = False
        self._value = value
        if needSendSignal:
            self.valueChanged.emit(value)

    def getCurrentValue(self) -> QPoint:
        return self._value

    def Type(self) -> int:
        return AttributeTypes.t_position2d
