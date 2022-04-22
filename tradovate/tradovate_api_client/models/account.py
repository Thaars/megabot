import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.account_account_type import AccountAccountType
from ..models.account_legal_status import AccountLegalStatus
from ..models.account_margin_account_type import AccountMarginAccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@attr.s(auto_attribs=True)
class Account:
    """
    Attributes:
        name (str):
        user_id (int):
        account_type (AccountAccountType): Customer, Giveup, House, Omnibus, Wash
        active (bool):
        clearing_house_id (int):
        risk_category_id (int):
        auto_liq_profile_id (int):
        margin_account_type (AccountMarginAccountType): Hedger, Speculator
        legal_status (AccountLegalStatus): Corporation, GP, IRA, Individual, Joint, LLC, LLP, LP, Trust
        timestamp (datetime.datetime):
        id (Union[Unset, int]):
        readonly (Union[Unset, bool]):
    """

    name: str
    user_id: int
    account_type: AccountAccountType
    active: bool
    clearing_house_id: int
    risk_category_id: int
    auto_liq_profile_id: int
    margin_account_type: AccountMarginAccountType
    legal_status: AccountLegalStatus
    timestamp: datetime.datetime
    id: Union[Unset, int] = UNSET
    readonly: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        user_id = self.user_id
        account_type = self.account_type.value

        active = self.active
        clearing_house_id = self.clearing_house_id
        risk_category_id = self.risk_category_id
        auto_liq_profile_id = self.auto_liq_profile_id
        margin_account_type = self.margin_account_type.value

        legal_status = self.legal_status.value

        timestamp = self.timestamp.isoformat()

        id = self.id
        readonly = self.readonly

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "userId": user_id,
                "accountType": account_type,
                "active": active,
                "clearingHouseId": clearing_house_id,
                "riskCategoryId": risk_category_id,
                "autoLiqProfileId": auto_liq_profile_id,
                "marginAccountType": margin_account_type,
                "legalStatus": legal_status,
                "timestamp": timestamp,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if readonly is not UNSET:
            field_dict["readonly"] = readonly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        user_id = d.pop("userId")

        account_type = AccountAccountType(d.pop("accountType"))

        active = d.pop("active")

        clearing_house_id = d.pop("clearingHouseId")

        risk_category_id = d.pop("riskCategoryId")

        auto_liq_profile_id = d.pop("autoLiqProfileId")

        margin_account_type = AccountMarginAccountType(d.pop("marginAccountType"))

        legal_status = AccountLegalStatus(d.pop("legalStatus"))

        timestamp = isoparse(d.pop("timestamp"))

        id = d.pop("id", UNSET)

        readonly = d.pop("readonly", UNSET)

        account = cls(
            name=name,
            user_id=user_id,
            account_type=account_type,
            active=active,
            clearing_house_id=clearing_house_id,
            risk_category_id=risk_category_id,
            auto_liq_profile_id=auto_liq_profile_id,
            margin_account_type=margin_account_type,
            legal_status=legal_status,
            timestamp=timestamp,
            id=id,
            readonly=readonly,
        )

        account.additional_properties = d
        return account

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
