from qtpy.QtCore import QObject
from typing import List, Optional, Union

from .NDAttributeGroup import NDAttributeGroup
from .NDAttributeBase import NDAttributeBase, NDAttributeFactory

NodeTypes = {
    "t_textNode": 0,
    "t_RectNode": 1,
    "t_Ellipse": 2,
    "t_Arrow": 3,
    "t_FreeDraw": 4,
    "t_User": 5,
    "t_End": 6,
}


# noinspection PyPep8Naming
class NDNodeBase(QObject):
    def __init__(self, nodeType: int = 0, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._nodeType = nodeType
        self._groupList: List[NDAttributeGroup] = []
        self._nodeName = ""

    def setNodeType(self, nodeType: int):
        self._nodeType = nodeType

    def getNodeType(self) -> int:
        return self._nodeType

    def setNodeName(self, nodeName: str):
        self._nodeName = nodeName

    def getNodeName(self) -> str:
        return self._nodeName

    def getAllAttributeGroups(self) -> List[NDAttributeGroup]:
        return self._groupList.copy()

    def addAttributeGroup(
        self, group: Union[NDAttributeGroup, str], displayName: Optional[str] = None
    ) -> Optional[NDAttributeGroup]:
        if not isinstance(group, (NDAttributeGroup, str)):
            return None

        if group is None:
            return None

        if group in self._groupList:
            return group

        if isinstance(group, str):
            groupName = group
            group = NDAttributeGroup()
            group.setName(groupName)
            if displayName:
                group.setDisplayName(groupName)
        group.setParentNode(self)
        self._groupList.append(group)
        return group

    def deleteAttributeGroup(self, group: Optional[NDAttributeGroup, str]):
        if isinstance(group, str):
            group = self.getAttributeGroup(group)
        if group in self._groupList:
            self._groupList.remove(group)
            group.deleteLater()

    def getAttributeGroup(self, name: str) -> Optional[NDAttributeGroup]:
        for group in self._groupList:
            if group.getName() == name:
                return group
        return None

    def addAttribute(
        self, group: Union[NDAttributeGroup, str], attribute: NDAttributeBase
    ) -> bool:
        if not group or attribute is None:
            return False
        if isinstance(group, str):
            group = self.getAttributeGroup(group)
            if not group:
                return False
        group.addAttribute(attribute)
        attribute.setParentNode(self)
        return True

    def addAttributeWithType(self, groupName: str, name: str, attrType: int) -> bool:
        attribute = NDAttributeFactory.createAttribute(name, attrType)
        if not attribute:
            return False
        return self.addAttribute(groupName, attribute)

    def deleteAttribute(self, attribute: Union[NDAttributeBase, str]) -> bool:
        if not attribute:
            return False
        if isinstance(attribute, str):
            attribute = self.getAttribute(attribute)
            if not attribute:
                return False
        group = attribute.getParentGroup()
        if not group:
            return False
        group.deleteAttribute(attribute)
        return True

    def getAttribute(self, attrName: str) -> Optional[NDAttributeBase]:
        for group in self._groupList:
            attribute = group.getAttribute(attrName)
            if attribute:
                return attribute
        return None
