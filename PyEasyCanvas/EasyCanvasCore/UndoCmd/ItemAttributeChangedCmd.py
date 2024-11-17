from typing import List, Any, Union

from qtpy.QtWidgets import QUndoCommand

from ...NDNodeAttribute.NDAttributeGroup import NDAttributeBase


# noinspection PyPep8Naming
class ItemAttributeChangedCmd(QUndoCommand):
    def __init__(
        self,
        attributeList: List[NDAttributeBase],
        value: Union[Any, List[Any]],
        canRun: bool = False,
    ):
        super().__init__()
        self._attributeList = []
        self._oldValueList = [value]
        self._newValueList = []
        self._isCanRun = canRun

    def undo(self):
        pass

    def redo(self):
        pass
