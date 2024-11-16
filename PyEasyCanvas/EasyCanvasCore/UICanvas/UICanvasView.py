import os
from typing import Optional

from qtpy.QtCore import QRect, Signal, QSize, Qt
from qtpy.QtGui import QPainter, QPen, QPixmap, QImage, QColor
from qtpy.QtWidgets import QGraphicsView, QWidget

from .UICanvasItemManager import UICanvasItemManager, g_currentCanvasManager
from .UICanvasOperators import UICanvasOperator, UICanvasDefaultOper
from .UICanvasPathItem import UICanvasPathItem
from .UICanvasScene import UICanvasScene
from ...utils import ASSETS_DIR


# noinspection PyPep8Naming
class UICanvasView(QGraphicsView):
    t_ArrowMode = 0
    t_FreeDrawMode = 1
    t_ImageMode = 2

    itemSelectedChanged = Signal()

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)
        self._scene: Optional[UICanvasScene] = None
        self._pathItem: Optional[UICanvasPathItem] = None
        self._currentOper: Optional[UICanvasOperator] = None
        self._isSelectedRectVisible: bool = False
        self._selectedRect: Optional[QRect] = None
        self._cSelectedPenColor: QColor = QColor(200, 100, 100)
        self._cSelectedBrushColor: QColor = QColor(0, 0, 200, 100)
        self._mode = self.t_ArrowMode
        self._penPixmap: Optional[QPixmap] = None

        UICanvasItemManager.createCanvasManager()
        UICanvasItemManager.setCurrentIndex(0)
        g_currentCanvasManager.setCurrentCanvasView(self)

        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self._scene = UICanvasScene()
        self._scene.selectionChanged.connect(self.itemSelectedChanged)
        self.setScene(self._scene)

        self.setCurrentOperator(UICanvasDefaultOper(self))

        initialPenImagePath = os.path.join(ASSETS_DIR, "freeDrawItem.png")
        self._penPixmap = QPixmap()
        self._penPixmap.load(initialPenImagePath)

    def createImageItem(self):
        g_currentCanvasManager.createCanvasItemByCmd(UICanvasItemManager.t_ImageItem)

    def createTextItem(self):
        g_currentCanvasManager.createCanvasItemByCmd(UICanvasItemManager.t_TextItem)

    def createRectItem(self):
        g_currentCanvasManager.createCanvasItemByCmd(UICanvasItemManager.t_RectItem)

    def createEllipseItem(self):
        g_currentCanvasManager.createCanvasItemByCmd(UICanvasItemManager.t_EllipseItem)

    def setSelectedRectVisible(self, visible: bool):
        self._isSelectedRectVisible = visible
        self.viewport().update()

    def setSelectedRect(self, rect: QRect):
        pass

    def moseMoveEvent(self, event):
        pass

    def mousePressEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

    def wheelEvent(self, event):
        pass

    def keyPressEvent(self, event):
        pass

    def keyReleaseEvent(self, event):
        pass

    def setCurrentOperator(self, oper: UICanvasOperator):
        self._currentOper = oper
        self._currentOper.setCanvasView(self)
