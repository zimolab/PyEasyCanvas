from typing import Optional

from qtpy.QtCore import QObject

from .NDBoolAttribute import NDBoolAttribute
from .NDColorAttribute import NDColorAttribute
from .NDIntAttribute import NDIntAttribute
from .NDNodeBase import NDNodeBase, NodeTypes
from .NDRealAttribute import NDRealAttribute
from .NDStringAttribute import NDStringAttribute


class NDTextNode(NDNodeBase):
    def __init(self, parent: Optional[QObject] = None):
        super().__init__(nodeType=NodeTypes["t_textNode"], parent=parent)

        self._positionXAttr: Optional[NDRealAttribute] = NDRealAttribute(self)
        self._positionYAttr: Optional[NDRealAttribute] = NDRealAttribute(self)
        self._textAttr: Optional[NDStringAttribute] = NDStringAttribute(self)
        self._textColorAttr: Optional[NDColorAttribute] = NDColorAttribute(self)
        self._fontSizeAttr: Optional[NDIntAttribute] = NDIntAttribute(self)
        self._fontFamilyAttr: Optional[NDStringAttribute] = NDStringAttribute(self)

        self._outlineSwitchAttr: Optional[NDBoolAttribute] = NDBoolAttribute(self)
        self._outlineWidthAttr: Optional[NDIntAttribute] = NDIntAttribute(self)
        self._outlineColorAttr: Optional[NDColorAttribute] = NDColorAttribute(self)

        self._initAttribute()

    def getXPositionAttr(self) -> Optional[NDRealAttribute]:
        return self._positionXAttr

    def getYPositionAttr(self) -> Optional[NDRealAttribute]:
        return self._positionYAttr

    def getTextAttr(self) -> Optional[NDStringAttribute]:
        return self._textAttr

    def getTextColorAttr(self) -> Optional[NDColorAttribute]:
        return self._textColorAttr

    def _initAttribute(self):
        self._positionXAttr.setName("XPosition")
        self._positionXAttr.setDisplayName("X Position")

        self._positionYAttr.setName("YPosition")
        self._positionYAttr.setDisplayName("Y Position")

        self._textAttr.setName("text")
        self._textAttr.setDisplayName("Text")

        self._textColorAttr.setName("textColor")
        self._textColorAttr.setDisplayName("Text Color")
