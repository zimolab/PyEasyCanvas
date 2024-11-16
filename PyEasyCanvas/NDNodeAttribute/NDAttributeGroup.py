from typing import ForwardRef, Optional, List

from qtpy.QtCore import QObject

NDAttributeBase = ForwardRef("NDAttributeBase")
NDNodeBase = ForwardRef("NDNodeBase")


class NDAttributeGroup(QObject):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._parentNode: Optional[NDNodeBase] = None
        self._attributes: List[NDAttributeBase] = []
        self._groupName: str = ""
        self._displayName: str = ""

    def addAttribute(self, attribute: NDAttributeBase):
        if attribute in self._attributes:
            return
        attribute.setParentGroup(self)
        self._attributes.append(attribute)

    def deleteAttribute(self, attribute: NDAttributeBase):
        if attribute not in self._attributes:
            return
        self._attributes.remove(attribute)
        attribute.deleteLater()

    def getAttributes(self) -> List[NDAttributeBase]:
        return self._attributes.copy()

    def getAttribute(self, name: str) -> Optional[NDAttributeBase]:
        for attribute in self._attributes:
            attribute: NDAttributeBase
            if attribute.getName() == name:
                return attribute
        return None

    def setParentNode(self, node: NDNodeBase):
        self._parentNode = node
        self.setParent(node)

    def getParentNode(self) -> Optional[NDNodeBase]:
        return self._parentNode

    def setName(self, name: str):
        self._groupName = name

    def getName(self) -> str:
        return self._groupName

    def setDisplayName(self, name: str):
        self._displayName = name

    def getDisplayName(self) -> str:
        return self._displayName
