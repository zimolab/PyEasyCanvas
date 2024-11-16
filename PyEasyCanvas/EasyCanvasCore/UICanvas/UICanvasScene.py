from typing import Optional, Any

from qtpy.QtCore import Signal, QObject
from qtpy.QtWidgets import QGraphicsScene

from ...NDNodeAttribute.NDNodeBase import NDNodeBase


class UICanvasScene(QGraphicsScene):

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

    def drawBackground(self, painter, rect):
        pass

    def drawForeground(self, painter, rect):
        pass

    def getCurrentNode(self) -> Optional[NDNodeBase]:
        pass

    def resetNodeInfo(self):
        pass

    def onWidthAttributeValueChanged(self, value: Any):
        pass

    def onHeightAttributeValueChanged(self, value: Any):
        pass

    def onColorAttributeValueChanged(self, value: Any):
        pass
