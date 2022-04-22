import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAccountAutoLiq")


@attr.s(auto_attribs=True)
class UserAccountAutoLiq:
    """
    Attributes:
        id (Union[Unset, int]):
        changes_locked (Union[Unset, bool]): Changes Locked
        margin_percentage_alert (Union[Unset, float]): Margin % for an Alert
        daily_loss_percentage_alert (Union[Unset, float]): Daily Loss % for an Alert
        daily_loss_alert (Union[Unset, float]): $ Daily Loss for an Alert
        margin_percentage_liq_only (Union[Unset, float]): Margin % for an Liq Only
        daily_loss_percentage_liq_only (Union[Unset, float]): Daily Loss % for an Liq Only
        daily_loss_liq_only (Union[Unset, float]): $ Daily Loss for an Liq Only
        margin_percentage_auto_liq (Union[Unset, float]): Margin % for an Auto-Liq
        daily_loss_percentage_auto_liq (Union[Unset, float]): Daily Loss % for an AutoLiq
        daily_loss_auto_liq (Union[Unset, float]): $ Daily Loss for an Auto-Liq
        weekly_loss_auto_liq (Union[Unset, float]): $ Weekly Loss for an Auto-Liq
        flatten_timestamp (Union[Unset, datetime.datetime]): Flatten &amp; Cancel
        trailing_max_drawdown (Union[Unset, float]): $ Trailing Max Drawdown
        trailing_max_drawdown_limit (Union[Unset, float]): $ Trailing Max Drawdown Limit
        daily_profit_auto_liq (Union[Unset, float]): $ Daily Profit for an Auto-Liq
        weekly_profit_auto_liq (Union[Unset, float]): $ Weekly Profit for an Auto-Liq
    """

    id: Union[Unset, int] = UNSET
    changes_locked: Union[Unset, bool] = UNSET
    margin_percentage_alert: Union[Unset, float] = UNSET
    daily_loss_percentage_alert: Union[Unset, float] = UNSET
    daily_loss_alert: Union[Unset, float] = UNSET
    margin_percentage_liq_only: Union[Unset, float] = UNSET
    daily_loss_percentage_liq_only: Union[Unset, float] = UNSET
    daily_loss_liq_only: Union[Unset, float] = UNSET
    margin_percentage_auto_liq: Union[Unset, float] = UNSET
    daily_loss_percentage_auto_liq: Union[Unset, float] = UNSET
    daily_loss_auto_liq: Union[Unset, float] = UNSET
    weekly_loss_auto_liq: Union[Unset, float] = UNSET
    flatten_timestamp: Union[Unset, datetime.datetime] = UNSET
    trailing_max_drawdown: Union[Unset, float] = UNSET
    trailing_max_drawdown_limit: Union[Unset, float] = UNSET
    daily_profit_auto_liq: Union[Unset, float] = UNSET
    weekly_profit_auto_liq: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        changes_locked = self.changes_locked
        margin_percentage_alert = self.margin_percentage_alert
        daily_loss_percentage_alert = self.daily_loss_percentage_alert
        daily_loss_alert = self.daily_loss_alert
        margin_percentage_liq_only = self.margin_percentage_liq_only
        daily_loss_percentage_liq_only = self.daily_loss_percentage_liq_only
        daily_loss_liq_only = self.daily_loss_liq_only
        margin_percentage_auto_liq = self.margin_percentage_auto_liq
        daily_loss_percentage_auto_liq = self.daily_loss_percentage_auto_liq
        daily_loss_auto_liq = self.daily_loss_auto_liq
        weekly_loss_auto_liq = self.weekly_loss_auto_liq
        flatten_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.flatten_timestamp, Unset):
            flatten_timestamp = self.flatten_timestamp.isoformat()

        trailing_max_drawdown = self.trailing_max_drawdown
        trailing_max_drawdown_limit = self.trailing_max_drawdown_limit
        daily_profit_auto_liq = self.daily_profit_auto_liq
        weekly_profit_auto_liq = self.weekly_profit_auto_liq

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if changes_locked is not UNSET:
            field_dict["changesLocked"] = changes_locked
        if margin_percentage_alert is not UNSET:
            field_dict["marginPercentageAlert"] = margin_percentage_alert
        if daily_loss_percentage_alert is not UNSET:
            field_dict["dailyLossPercentageAlert"] = daily_loss_percentage_alert
        if daily_loss_alert is not UNSET:
            field_dict["dailyLossAlert"] = daily_loss_alert
        if margin_percentage_liq_only is not UNSET:
            field_dict["marginPercentageLiqOnly"] = margin_percentage_liq_only
        if daily_loss_percentage_liq_only is not UNSET:
            field_dict["dailyLossPercentageLiqOnly"] = daily_loss_percentage_liq_only
        if daily_loss_liq_only is not UNSET:
            field_dict["dailyLossLiqOnly"] = daily_loss_liq_only
        if margin_percentage_auto_liq is not UNSET:
            field_dict["marginPercentageAutoLiq"] = margin_percentage_auto_liq
        if daily_loss_percentage_auto_liq is not UNSET:
            field_dict["dailyLossPercentageAutoLiq"] = daily_loss_percentage_auto_liq
        if daily_loss_auto_liq is not UNSET:
            field_dict["dailyLossAutoLiq"] = daily_loss_auto_liq
        if weekly_loss_auto_liq is not UNSET:
            field_dict["weeklyLossAutoLiq"] = weekly_loss_auto_liq
        if flatten_timestamp is not UNSET:
            field_dict["flattenTimestamp"] = flatten_timestamp
        if trailing_max_drawdown is not UNSET:
            field_dict["trailingMaxDrawdown"] = trailing_max_drawdown
        if trailing_max_drawdown_limit is not UNSET:
            field_dict["trailingMaxDrawdownLimit"] = trailing_max_drawdown_limit
        if daily_profit_auto_liq is not UNSET:
            field_dict["dailyProfitAutoLiq"] = daily_profit_auto_liq
        if weekly_profit_auto_liq is not UNSET:
            field_dict["weeklyProfitAutoLiq"] = weekly_profit_auto_liq

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        changes_locked = d.pop("changesLocked", UNSET)

        margin_percentage_alert = d.pop("marginPercentageAlert", UNSET)

        daily_loss_percentage_alert = d.pop("dailyLossPercentageAlert", UNSET)

        daily_loss_alert = d.pop("dailyLossAlert", UNSET)

        margin_percentage_liq_only = d.pop("marginPercentageLiqOnly", UNSET)

        daily_loss_percentage_liq_only = d.pop("dailyLossPercentageLiqOnly", UNSET)

        daily_loss_liq_only = d.pop("dailyLossLiqOnly", UNSET)

        margin_percentage_auto_liq = d.pop("marginPercentageAutoLiq", UNSET)

        daily_loss_percentage_auto_liq = d.pop("dailyLossPercentageAutoLiq", UNSET)

        daily_loss_auto_liq = d.pop("dailyLossAutoLiq", UNSET)

        weekly_loss_auto_liq = d.pop("weeklyLossAutoLiq", UNSET)

        _flatten_timestamp = d.pop("flattenTimestamp", UNSET)
        flatten_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_flatten_timestamp, Unset):
            flatten_timestamp = UNSET
        else:
            flatten_timestamp = isoparse(_flatten_timestamp)

        trailing_max_drawdown = d.pop("trailingMaxDrawdown", UNSET)

        trailing_max_drawdown_limit = d.pop("trailingMaxDrawdownLimit", UNSET)

        daily_profit_auto_liq = d.pop("dailyProfitAutoLiq", UNSET)

        weekly_profit_auto_liq = d.pop("weeklyProfitAutoLiq", UNSET)

        user_account_auto_liq = cls(
            id=id,
            changes_locked=changes_locked,
            margin_percentage_alert=margin_percentage_alert,
            daily_loss_percentage_alert=daily_loss_percentage_alert,
            daily_loss_alert=daily_loss_alert,
            margin_percentage_liq_only=margin_percentage_liq_only,
            daily_loss_percentage_liq_only=daily_loss_percentage_liq_only,
            daily_loss_liq_only=daily_loss_liq_only,
            margin_percentage_auto_liq=margin_percentage_auto_liq,
            daily_loss_percentage_auto_liq=daily_loss_percentage_auto_liq,
            daily_loss_auto_liq=daily_loss_auto_liq,
            weekly_loss_auto_liq=weekly_loss_auto_liq,
            flatten_timestamp=flatten_timestamp,
            trailing_max_drawdown=trailing_max_drawdown,
            trailing_max_drawdown_limit=trailing_max_drawdown_limit,
            daily_profit_auto_liq=daily_profit_auto_liq,
            weekly_profit_auto_liq=weekly_profit_auto_liq,
        )

        user_account_auto_liq.additional_properties = d
        return user_account_auto_liq

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
