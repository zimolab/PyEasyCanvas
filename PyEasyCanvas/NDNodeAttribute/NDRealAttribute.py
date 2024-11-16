from typing import ForwardRef, Optional, Tuple

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


# noinspection PyPep8Naming
class NDRealAttribute(NDAttributeBase):
    def __init__(self, parentNode: Optional[NDNodeBase] = None):
        super().__init__(parentNode)

        self._minValue: float = 0.0
        self._maxValue: float = 100.0

        self._value = 0.0

    def Type(self) -> int:
        return AttributeTypes.t_qreal

    def setValueRange(self, minValue: float, maxValue: float):
        self._minValue = minValue
        self._maxValue = maxValue

    def getValueRange(self) -> Tuple[float, float]:
        return self._minValue, self._maxValue
