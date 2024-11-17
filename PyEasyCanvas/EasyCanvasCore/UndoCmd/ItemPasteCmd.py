from typing import List

from qtpy.QtWidgets import QUndoCommand

from ..UICanvas.UICanvasItemBase import UICanvasItemBase
from ..UICanvas.UICanvasItemManager import g_currentCanvasManager


class ItemPasteCmd(QUndoCommand):
    def __init__(self):
        super().__init__()

        self._createdItems: List[UICanvasItemBase] = []

        self.setText("Paste Cmd")

    def redo(self):
        for item in self._createdItems:
            node = item.getCurrentNode()
            g_currentCanvasManager.deleteCanvasItem(node)

    def undo(self):
        if len(self._createdItems) <= 0:
            g_currentCanvasManager.paste()
            return
        for item in self._createdItems:
            g_currentCanvasManager.addCanvasItem(item)
