from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RevokeTradingPermission")


@attr.s(auto_attribs=True)
class RevokeTradingPermission:
    """
    Attributes:
        trading_permission_id (int):
    """

    trading_permission_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trading_permission_id = self.trading_permission_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tradingPermissionId": trading_permission_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trading_permission_id = d.pop("tradingPermissionId")

        revoke_trading_permission = cls(
            trading_permission_id=trading_permission_id,
        )

        revoke_trading_permission.additional_properties = d
        return revoke_trading_permission

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
