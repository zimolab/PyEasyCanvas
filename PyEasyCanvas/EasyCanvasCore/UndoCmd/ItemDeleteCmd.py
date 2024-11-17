from typing import List

from qtpy.QtWidgets import QUndoCommand

from ..UICanvas.UICanvasItemBase import UICanvasItemBase
from ..UICanvas.UICanvasItemManager import g_currentCanvasManager


# noinspection PyPep8Naming
class ItemDeleteCmd(QUndoCommand):
    def __init__(self, items: List[UICanvasItemBase]):
        super().__init__()

        self._items = items

        nodeNames = []
        for item in self._items:
            name = item.getCurrentNode().getNodeName()
            nodeNames.append(name)

        if nodeNames:
            self.setText(",".join(nodeNames))

    def redo(self):
        nodeNames = []
        for item in self._items:
            if item is None:
                continue
            nodeNames.append(g_currentCanvasManager.getCurrentNode(item).getNodeName())
        g_currentCanvasManager.deleteCanvasItems(nodeNames)

    def undo(self):
        for item in self._items:
            if item is None:
                continue
            g_currentCanvasManager.addCanvasItem(item)
