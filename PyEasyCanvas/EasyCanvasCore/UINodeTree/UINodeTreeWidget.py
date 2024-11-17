from typing import List, Optional, Any, Union

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QAction, QUndoStack, QUndoView


from ...NDNodeAttribute.NDAttributeBase import NDAttributeBase


class UndoCmdType:
    t_createCmd = 0
    t_deleteCmd = 1
    t_renameCmd = 2
    t_changedAttrCmd = 3
    t_pasteCmd = 4


# noinspection PyPep8Naming
class UndoCmdCore(QObject):

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        self._undoStack = QUndoStack(self)

    def runCreateCmd(self, cmdType: int):
        pass

    def runDeleteCmd(self, nodeNames: List[str]):
        pass

    def runChangeNameCmd(self, nodeName: str, destNodeName: str):
        pass

    def runChangedAttrCmd(
        self,
        attrs: Union[str, List[NDAttributeBase]],
        value: Union[Any, List[Any]],
        isCanrun: bool = False,
    ):
        if isinstance(attrs, str) and not isinstance(value, list):
            return self.runChangedAttrCmd1(attrs, value, isCanrun)

        if isinstance(attrs, list) and isinstance(value, list):
            return self.runChangedAttrCmd3(attrs, value, isCanrun)

        if isinstance(attrs, list) and not isinstance(value, list):
            return self.runChangedAttrCmd2(attrs, value, isCanrun)

        raise ValueError("invalid arguments")

    def runChangedAttrCmd1(self, attrFullName: str, value: Any, isCanrun: bool = False):
        pass

    def runChangedAttrCmd2(
        self, attrList: List[NDAttributeBase], value: Any, isCanrun: bool = False
    ):
        pass

    def runChangedAttrCmd3(
        self,
        attrList: List[NDAttributeBase],
        values: List[Any],
        isCanrun: bool = False,
    ):
        pass

    def runPasteCmd(self):
        pass

    def redo(self):
        self._undoStack.redo()

    def undo(self):
        self._undoStack.undo()

    def createRedoAction(self) -> QAction:
        return QAction("Redo", self)

    def createUndoAction(self) -> QAction:
        return QAction("Undo", self)

    def createUndoView(self) -> QUndoView:
        return QUndoView(self._undoStack)

    def isUndoStackEmpty(self) -> bool:
        return self._undoStack.isClean()

    def cleanUndoStack(self):
        self._undoStack.clear()
