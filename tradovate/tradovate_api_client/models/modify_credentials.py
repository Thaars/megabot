from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyCredentials")


@attr.s(auto_attribs=True)
class ModifyCredentials:
    """
    Attributes:
        name (str):
        password (str):
        current_password (str):
        user_id (Union[Unset, int]):
    """

    name: str
    password: str
    current_password: str
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        password = self.password
        current_password = self.current_password
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
                "currentPassword": current_password,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        password = d.pop("password")

        current_password = d.pop("currentPassword")

        user_id = d.pop("userId", UNSET)

        modify_credentials = cls(
            name=name,
            password=password,
            current_password=current_password,
            user_id=user_id,
        )

        modify_credentials.additional_properties = d
        return modify_credentials

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
