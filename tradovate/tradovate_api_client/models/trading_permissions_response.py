from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.trading_permission import TradingPermission

T = TypeVar("T", bound="TradingPermissionsResponse")


@attr.s(auto_attribs=True)
class TradingPermissionsResponse:
    """
    Attributes:
        trading_permissions (List[TradingPermission]):
    """

    trading_permissions: List[TradingPermission]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trading_permissions = []
        for trading_permissions_item_data in self.trading_permissions:
            trading_permissions_item = trading_permissions_item_data.to_dict()

            trading_permissions.append(trading_permissions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tradingPermissions": trading_permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trading_permissions = []
        _trading_permissions = d.pop("tradingPermissions")
        for trading_permissions_item_data in _trading_permissions:
            trading_permissions_item = TradingPermission.from_dict(trading_permissions_item_data)

            trading_permissions.append(trading_permissions_item)

        trading_permissions_response = cls(
            trading_permissions=trading_permissions,
        )

        trading_permissions_response.additional_properties = d
        return trading_permissions_response

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
