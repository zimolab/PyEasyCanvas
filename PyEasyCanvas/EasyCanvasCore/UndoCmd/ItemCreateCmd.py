from typing import Optional

from qtpy.QtWidgets import QUndoCommand

from ..UICanvas.UICanvasItemBase import UICanvasItemBase
from ..UICanvas.UICanvasItemManager import g_currentCanvasManager


# noinspection PyPep8Naming
class ItemCreateCmd(QUndoCommand):
    def __init__(self, cmdType: int):
        super().__init__()

        self._cmdType = cmdType
        self._canvasItem: Optional[UICanvasItemBase] = None

        name = g_currentCanvasManager.getNodeTypeDisplayName(self._cmdType)
        self.setText(f"Create Node {name}")

    def undo(self):
        if self._canvasItem is None:
            return
        node = self._canvasItem.getCurrentNode()
        g_currentCanvasManager.deleteCanvasItem(node)

    def redo(self):
        if self._canvasItem is None:
            self._canvasItem = g_currentCanvasManager.createCanvasItem(self._cmdType)
        else:
            g_currentCanvasManager.addCanvasItem(self._canvasItem)
