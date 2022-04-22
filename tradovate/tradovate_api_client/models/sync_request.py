from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncRequest")


@attr.s(auto_attribs=True)
class SyncRequest:
    """
    Attributes:
        users (Union[Unset, List[int]]):
        accounts (Union[Unset, List[int]]):
        split_responses (Union[Unset, bool]):
    """

    users: Union[Unset, List[int]] = UNSET
    accounts: Union[Unset, List[int]] = UNSET
    split_responses: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, List[int]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        accounts: Union[Unset, List[int]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = self.accounts

        split_responses = self.split_responses

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if split_responses is not UNSET:
            field_dict["splitResponses"] = split_responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        users = cast(List[int], d.pop("users", UNSET))

        accounts = cast(List[int], d.pop("accounts", UNSET))

        split_responses = d.pop("splitResponses", UNSET)

        sync_request = cls(
            users=users,
            accounts=accounts,
            split_responses=split_responses,
        )

        sync_request.additional_properties = d
        return sync_request

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
