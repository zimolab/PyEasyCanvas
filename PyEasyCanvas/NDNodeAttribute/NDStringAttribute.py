from typing import ForwardRef, Optional, Callable

from ._NDAttributeBase import NDAttributeBase, AttributeTypes

NDNodeBase = ForwardRef("NDNodeBase")


class NDStringAttribute(NDAttributeBase):
    def __init__(self, parentNode: Optional[NDNodeBase] = None):
        super().__init__(parentNode)
        self._value = ""

        self._isShowButton: bool = False
        self._buttonText: str = ""
        self._buttonCallback: Optional[Callable[[str], bool]] = None

    def Type(self) -> int:
        return AttributeTypes.t_string

    def setShowButton(self, isShow: bool):
        self._isShowButton = isShow

    def isShowButton(self) -> bool:
        return self._isShowButton

    def setButtonText(self, text: str):
        self._buttonText = text

    def getButtonText(self) -> str:
        return self._buttonText

    def setButtonCallback(self, callback: Callable[[str], bool]):
        self._buttonCallback = callback

    def getButtonCallback(self) -> Optional[Callable[[str], bool]]:
        return self._buttonCallback
