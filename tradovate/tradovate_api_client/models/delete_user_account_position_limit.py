from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DeleteUserAccountPositionLimit")


@attr.s(auto_attribs=True)
class DeleteUserAccountPositionLimit:
    """
    Attributes:
        user_account_position_limit_id (int):
    """

    user_account_position_limit_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_account_position_limit_id = self.user_account_position_limit_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userAccountPositionLimitId": user_account_position_limit_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_account_position_limit_id = d.pop("userAccountPositionLimitId")

        delete_user_account_position_limit = cls(
            user_account_position_limit_id=user_account_position_limit_id,
        )

        delete_user_account_position_limit.additional_properties = d
        return delete_user_account_position_limit

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
