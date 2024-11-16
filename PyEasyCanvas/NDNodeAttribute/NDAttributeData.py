from typing import Any


class NDAttributeData(object):

    def __init__(self):
        self._value: Any = None

    def setValue(self, value: Any):
        self._value = value

    def getValue(self) -> Any:
        return self._value
