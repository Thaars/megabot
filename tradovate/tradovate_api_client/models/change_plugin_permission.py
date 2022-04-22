from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePluginPermission")


@attr.s(auto_attribs=True)
class ChangePluginPermission:
    """
    Attributes:
        plugin_name (str):
        approval (bool):
        user_id (Union[Unset, int]):
    """

    plugin_name: str
    approval: bool
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        plugin_name = self.plugin_name
        approval = self.approval
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pluginName": plugin_name,
                "approval": approval,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        plugin_name = d.pop("pluginName")

        approval = d.pop("approval")

        user_id = d.pop("userId", UNSET)

        change_plugin_permission = cls(
            plugin_name=plugin_name,
            approval=approval,
            user_id=user_id,
        )

        change_plugin_permission.additional_properties = d
        return change_plugin_permission

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
