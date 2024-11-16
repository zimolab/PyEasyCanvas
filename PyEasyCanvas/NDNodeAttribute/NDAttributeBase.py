from typing import Optional

from .NDBoolAttribute import NDBoolAttribute
from .NDColorAttribute import NDColorAttribute
from .NDIntAttribute import NDIntAttribute
from .NDPostionAttribute import NDPosition2DAttribute
from .NDRealAttribute import NDRealAttribute
from .NDStringAttribute import NDStringAttribute
from ._NDAttributeBase import NDAttributeBase, AttributeTypes


# noinspection PyPep8Naming
class NDAttributeFactory(object):
    @staticmethod
    def createAttribute(
        name: str, attributeType: int, displayName=""
    ) -> Optional[NDAttributeBase]:
        attribute: Optional[NDAttributeBase] = None
        if attributeType == AttributeTypes.t_bool:
            attribute = NDBoolAttribute()
        elif attributeType == AttributeTypes.t_int:
            attribute = NDIntAttribute()
        elif attributeType == AttributeTypes.t_qreal:
            attribute = NDRealAttribute()
        elif attributeType == AttributeTypes.t_string:
            attribute = NDStringAttribute()
        # elif attributeType == AttributeTypes.t_stringList:
        #     attribute = NDStringListAttribute()
        elif attributeType == AttributeTypes.t_color:
            attribute = NDColorAttribute()
        elif attributeType == AttributeTypes.t_position2d:
            attribute = NDPosition2DAttribute()
        else:
            pass
        if attribute is None:
            return None
        attribute.setDisplayName(displayName)
        attribute.setName(name)
        return attribute
