from qtpy.QtWidgets import QUndoCommand

from ..UICanvas.UICanvasItemBase import UICanvasItemBase
from ..UICanvas.UICanvasItemManager import g_currentCanvasManager


# noinspection PyPep8Naming
class ItemChangeNameCmd(QUndoCommand):
    def __init__(self, item: UICanvasItemBase, destName: str):
        super().__init__()
        self._canvasItem = item
        self._destName = destName
        self._srcName = item.getCurrentNode().getNodeName()

        msg = f"Change name from {self._srcName} to {self._destName}"
        self.setText(msg)

    def undo(self):
        g_currentCanvasManager.changedNodeName(self._destName, self._srcName)

    def redo(self):
        g_currentCanvasManager.changedNodeName(self._srcName, self._destName)
