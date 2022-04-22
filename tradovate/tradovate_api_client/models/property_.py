from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.property_property_type import PropertyPropertyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Property")


@attr.s(auto_attribs=True)
class Property:
    """
    Attributes:
        name (str):
        property_type (PropertyPropertyType): Boolean, Enum, Integer, String
        id (Union[Unset, int]):
        enum_options (Union[Unset, str]):
        default_value (Union[Unset, str]):
    """

    name: str
    property_type: PropertyPropertyType
    id: Union[Unset, int] = UNSET
    enum_options: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        property_type = self.property_type.value

        id = self.id
        enum_options = self.enum_options
        default_value = self.default_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "propertyType": property_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if enum_options is not UNSET:
            field_dict["enumOptions"] = enum_options
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        property_type = PropertyPropertyType(d.pop("propertyType"))

        id = d.pop("id", UNSET)

        enum_options = d.pop("enumOptions", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        property_ = cls(
            name=name,
            property_type=property_type,
            id=id,
            enum_options=enum_options,
            default_value=default_value,
        )

        property_.additional_properties = d
        return property_

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
