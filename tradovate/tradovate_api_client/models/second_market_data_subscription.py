import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecondMarketDataSubscription")


@attr.s(auto_attribs=True)
class SecondMarketDataSubscription:
    """
    Attributes:
        user_id (int):
        timestamp (datetime.datetime):
        year (int):
        month (int):
        id (Union[Unset, int]):
        cancelled_renewal (Union[Unset, bool]):
        cancellation_timestamp (Union[Unset, datetime.datetime]):
    """

    user_id: int
    timestamp: datetime.datetime
    year: int
    month: int
    id: Union[Unset, int] = UNSET
    cancelled_renewal: Union[Unset, bool] = UNSET
    cancellation_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        timestamp = self.timestamp.isoformat()

        year = self.year
        month = self.month
        id = self.id
        cancelled_renewal = self.cancelled_renewal
        cancellation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_timestamp, Unset):
            cancellation_timestamp = self.cancellation_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "timestamp": timestamp,
                "year": year,
                "month": month,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if cancelled_renewal is not UNSET:
            field_dict["cancelledRenewal"] = cancelled_renewal
        if cancellation_timestamp is not UNSET:
            field_dict["cancellationTimestamp"] = cancellation_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        timestamp = isoparse(d.pop("timestamp"))

        year = d.pop("year")

        month = d.pop("month")

        id = d.pop("id", UNSET)

        cancelled_renewal = d.pop("cancelledRenewal", UNSET)

        _cancellation_timestamp = d.pop("cancellationTimestamp", UNSET)
        cancellation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_cancellation_timestamp, Unset):
            cancellation_timestamp = UNSET
        else:
            cancellation_timestamp = isoparse(_cancellation_timestamp)

        second_market_data_subscription = cls(
            user_id=user_id,
            timestamp=timestamp,
            year=year,
            month=month,
            id=id,
            cancelled_renewal=cancelled_renewal,
            cancellation_timestamp=cancellation_timestamp,
        )

        second_market_data_subscription.additional_properties = d
        return second_market_data_subscription

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
