from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CashBalanceSnapshot")


@attr.s(auto_attribs=True)
class CashBalanceSnapshot:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        total_cash_value (Union[Unset, float]):
        total_pn_l (Union[Unset, float]):
        initial_margin (Union[Unset, float]):
        maintenance_margin (Union[Unset, float]):
        net_liq (Union[Unset, float]):
        open_pn_l (Union[Unset, float]):
        realized_pn_l (Union[Unset, float]):
        week_realized_pn_l (Union[Unset, float]):
    """

    error_text: Union[Unset, str] = UNSET
    total_cash_value: Union[Unset, float] = UNSET
    total_pn_l: Union[Unset, float] = UNSET
    initial_margin: Union[Unset, float] = UNSET
    maintenance_margin: Union[Unset, float] = UNSET
    net_liq: Union[Unset, float] = UNSET
    open_pn_l: Union[Unset, float] = UNSET
    realized_pn_l: Union[Unset, float] = UNSET
    week_realized_pn_l: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        total_cash_value = self.total_cash_value
        total_pn_l = self.total_pn_l
        initial_margin = self.initial_margin
        maintenance_margin = self.maintenance_margin
        net_liq = self.net_liq
        open_pn_l = self.open_pn_l
        realized_pn_l = self.realized_pn_l
        week_realized_pn_l = self.week_realized_pn_l

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if total_cash_value is not UNSET:
            field_dict["totalCashValue"] = total_cash_value
        if total_pn_l is not UNSET:
            field_dict["totalPnL"] = total_pn_l
        if initial_margin is not UNSET:
            field_dict["initialMargin"] = initial_margin
        if maintenance_margin is not UNSET:
            field_dict["maintenanceMargin"] = maintenance_margin
        if net_liq is not UNSET:
            field_dict["netLiq"] = net_liq
        if open_pn_l is not UNSET:
            field_dict["openPnL"] = open_pn_l
        if realized_pn_l is not UNSET:
            field_dict["realizedPnL"] = realized_pn_l
        if week_realized_pn_l is not UNSET:
            field_dict["weekRealizedPnL"] = week_realized_pn_l

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        total_cash_value = d.pop("totalCashValue", UNSET)

        total_pn_l = d.pop("totalPnL", UNSET)

        initial_margin = d.pop("initialMargin", UNSET)

        maintenance_margin = d.pop("maintenanceMargin", UNSET)

        net_liq = d.pop("netLiq", UNSET)

        open_pn_l = d.pop("openPnL", UNSET)

        realized_pn_l = d.pop("realizedPnL", UNSET)

        week_realized_pn_l = d.pop("weekRealizedPnL", UNSET)

        cash_balance_snapshot = cls(
            error_text=error_text,
            total_cash_value=total_cash_value,
            total_pn_l=total_pn_l,
            initial_margin=initial_margin,
            maintenance_margin=maintenance_margin,
            net_liq=net_liq,
            open_pn_l=open_pn_l,
            realized_pn_l=realized_pn_l,
            week_realized_pn_l=week_realized_pn_l,
        )

        cash_balance_snapshot.additional_properties = d
        return cash_balance_snapshot

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
