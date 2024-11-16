from abc import abstractmethod
from typing import ForwardRef, Optional, Any

from qtpy.QtCore import Signal, QObject

from .NDNodeManager import g_nodeManager

NDNodeBase = ForwardRef("NDNodeBase")
NDAttributeGroup = ForwardRef("NDAttributeGroup")


class AttributeTypes(object):
    t_bool = 0
    t_int = 1
    t_qreal = 2
    t_string = 3
    t_stringList = 4
    t_color = 5
    t_position2d = 6


AttributeTypeNames = {
    AttributeTypes.t_bool: "Bool",
    AttributeTypes.t_int: "Int",
    AttributeTypes.t_qreal: "QReal",
    AttributeTypes.t_string: "String",
    AttributeTypes.t_stringList: "StringList",
    AttributeTypes.t_color: "Color",
    AttributeTypes.t_position2d: "Position2D",
}


# noinspection PyPep8Naming
class NDAttributeBase(QObject):
    enabledChanged = Signal(bool)
    valueChanged = Signal(object, bool)

    def __init__(self, parentNode: Optional[NDNodeBase] = None):
        super().__init__(parentNode)
        self._attributeType: int = -1
        self._attributeName: str = ""
        self._displayName: str = ""
        self._isEnabled: bool = True
        self._lastValue: Any = None
        self._value: Any = None
        self._isFirstSetValue: bool = True
        self._parentGroup: Optional[NDAttributeGroup] = None
        self._parentNode: Optional[NDNodeBase] = parentNode

        # noinspection PyUnresolvedReferences
        self.valueChanged.connect(self.onValueChanged)

    @abstractmethod
    def Type(self) -> int:
        raise NotImplementedError("Subclasses should implement this method.")

    def getLastValue(self) -> Any:
        return self._lastValue

    def getTypeName(self) -> str:
        return AttributeTypeNames.get(self.Type(), "")

    def setValue(self, value: Any, cmd: bool = False):
        if self._isFirstSetValue:
            self._lastValue = value
            self._isFirstSetValue = False
        needSendSignal = self._value != value
        tmp = self._value
        self._value = value
        if needSendSignal:
            self._lastValue = tmp
            # noinspection PyUnresolvedReferences
            self.valueChanged.emit(value, cmd)

    def getValue(self) -> Any:
        return self._value

    def setName(self, name: str):
        self._attributeName = name
        if self._displayName.strip() == "":
            self._displayName = name

    def getName(self) -> str:
        return self._attributeName

    def setDisplayName(self, name: str):
        self._displayName = name

    def getDisplayName(self) -> str:
        return self._displayName

    def getFullName(self) -> str:
        if self._parentNode is None:
            return ""
        return self._parentNode.getNodeName() + "." + self._attributeName

    def setParentGroup(self, group: Optional[NDAttributeGroup]):
        if group is None:
            return
        self.setParent(group)
        self._parentGroup = group

    def getParentGroup(self) -> Optional[NDAttributeGroup]:
        return self._parentGroup

    def setParentNode(self, node: Optional[NDNodeBase]):
        self._parentNode = node

    def getParentNode(self) -> Optional[NDNodeBase]:
        return self._parentNode

    def setEnable(self, isEnabled: bool):
        if self._isEnabled == isEnabled:
            return
        self._isEnabled = isEnabled
        # noinspection PyUnresolvedReferences
        self.enabledChanged.emit(isEnabled)

    def isEnable(self) -> bool:
        return self._isEnabled

    def onValueChanged(self, value: Any, cmd: bool = False):
        g_nodeManager.onAttributeChanged(self, value, cmd)
