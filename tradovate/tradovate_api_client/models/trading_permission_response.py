from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trading_permission import TradingPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradingPermissionResponse")


@attr.s(auto_attribs=True)
class TradingPermissionResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        trading_permission (Union[Unset, TradingPermission]):
    """

    error_text: Union[Unset, str] = UNSET
    trading_permission: Union[Unset, TradingPermission] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        trading_permission: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trading_permission, Unset):
            trading_permission = self.trading_permission.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if trading_permission is not UNSET:
            field_dict["tradingPermission"] = trading_permission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _trading_permission = d.pop("tradingPermission", UNSET)
        trading_permission: Union[Unset, TradingPermission]
        if isinstance(_trading_permission, Unset):
            trading_permission = UNSET
        else:
            trading_permission = TradingPermission.from_dict(_trading_permission)

        trading_permission_response = cls(
            error_text=error_text,
            trading_permission=trading_permission,
        )

        trading_permission_response.additional_properties = d
        return trading_permission_response

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
