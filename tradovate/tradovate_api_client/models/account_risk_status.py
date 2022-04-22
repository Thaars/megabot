import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account_risk_status_admin_action import AccountRiskStatusAdminAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountRiskStatus")


@attr.s(auto_attribs=True)
class AccountRiskStatus:
    """
    Attributes:
        id (Union[Unset, int]):
        admin_action (Union[Unset, AccountRiskStatusAdminAction]): AgreedOnLiqOnlyModeByAutoLiq,
            AgreedOnLiquidationByAutoLiq, DisableAutoLiq, LiquidateImmediately, LiquidateOnlyModeImmediately,
            LockTradingImmediately, Normal, PlaceAutoLiqOnHold
        admin_timestamp (Union[Unset, datetime.datetime]):
        liquidate_only (Union[Unset, datetime.datetime]):
        user_triggered_liq_only (Union[Unset, bool]):
    """

    id: Union[Unset, int] = UNSET
    admin_action: Union[Unset, AccountRiskStatusAdminAction] = UNSET
    admin_timestamp: Union[Unset, datetime.datetime] = UNSET
    liquidate_only: Union[Unset, datetime.datetime] = UNSET
    user_triggered_liq_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        admin_action: Union[Unset, str] = UNSET
        if not isinstance(self.admin_action, Unset):
            admin_action = self.admin_action.value

        admin_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.admin_timestamp, Unset):
            admin_timestamp = self.admin_timestamp.isoformat()

        liquidate_only: Union[Unset, str] = UNSET
        if not isinstance(self.liquidate_only, Unset):
            liquidate_only = self.liquidate_only.isoformat()

        user_triggered_liq_only = self.user_triggered_liq_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if admin_action is not UNSET:
            field_dict["adminAction"] = admin_action
        if admin_timestamp is not UNSET:
            field_dict["adminTimestamp"] = admin_timestamp
        if liquidate_only is not UNSET:
            field_dict["liquidateOnly"] = liquidate_only
        if user_triggered_liq_only is not UNSET:
            field_dict["userTriggeredLiqOnly"] = user_triggered_liq_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _admin_action = d.pop("adminAction", UNSET)
        admin_action: Union[Unset, AccountRiskStatusAdminAction]
        if isinstance(_admin_action, Unset):
            admin_action = UNSET
        else:
            admin_action = AccountRiskStatusAdminAction(_admin_action)

        _admin_timestamp = d.pop("adminTimestamp", UNSET)
        admin_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_admin_timestamp, Unset):
            admin_timestamp = UNSET
        else:
            admin_timestamp = isoparse(_admin_timestamp)

        _liquidate_only = d.pop("liquidateOnly", UNSET)
        liquidate_only: Union[Unset, datetime.datetime]
        if isinstance(_liquidate_only, Unset):
            liquidate_only = UNSET
        else:
            liquidate_only = isoparse(_liquidate_only)

        user_triggered_liq_only = d.pop("userTriggeredLiqOnly", UNSET)

        account_risk_status = cls(
            id=id,
            admin_action=admin_action,
            admin_timestamp=admin_timestamp,
            liquidate_only=liquidate_only,
            user_triggered_liq_only=user_triggered_liq_only,
        )

        account_risk_status.additional_properties = d
        return account_risk_status

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
