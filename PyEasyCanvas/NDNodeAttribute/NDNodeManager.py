from typing import Optional, ForwardRef, Any

from qtpy.QtCore import QObject, Signal

NDNodeBase = ForwardRef("NDNodeBase")
NDAttributeBase = ForwardRef("NDAttributeBase")


class NDNodeManager(QObject):
    signalAttrValueChanged = Signal(object, object, bool)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

    def informAttributeValueChanged(
        self, attribute: NDAttributeBase, value: Any, cmd: bool = False
    ):
        # noinspection PyUnresolvedReferences
        self.signalAttrValueChanged.emit(attribute, value, cmd)


g_nodeManager = NDNodeManager()
