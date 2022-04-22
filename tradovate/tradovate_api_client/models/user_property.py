from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProperty")


@attr.s(auto_attribs=True)
class UserProperty:
    """
    Attributes:
        user_id (int):
        property_id (int):
        id (Union[Unset, int]):
        value (Union[Unset, str]):
    """

    user_id: int
    property_id: int
    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        property_id = self.property_id
        id = self.id
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "propertyId": property_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        property_id = d.pop("propertyId")

        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        user_property = cls(
            user_id=user_id,
            property_id=property_id,
            id=id,
            value=value,
        )

        user_property.additional_properties = d
        return user_property

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
