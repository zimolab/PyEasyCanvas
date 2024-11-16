from typing import ForwardRef, Optional, Tuple

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


# noinspection PyPep8Naming
class NDIntAttribute(NDAttributeBase):
    def __init__(self, parentNode: Optional[NDNodeBase] = None):
        super().__init__(parentNode)

        self._minValue: int = 0
        self._maxValue: int = 100

        self._value = 0

    def Type(self) -> int:
        return AttributeTypes.t_int

    def setValueRange(self, minValue: int, maxValue: int):
        self._minValue = minValue
        self._maxValue = maxValue

    def getValueRange(self) -> Tuple[int, int]:
        return self._minValue, self._maxValue
