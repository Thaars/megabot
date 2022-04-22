from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactInfo")


@attr.s(auto_attribs=True)
class ContactInfo:
    """
    Attributes:
        user_id (int):
        first_name (str):
        last_name (str):
        street_address_1 (str):
        city (str):
        country (str):
        phone (str):
        id (Union[Unset, int]):
        street_address_2 (Union[Unset, str]):
        state (Union[Unset, str]):
        post_code (Union[Unset, str]):
        mailing_is_different (Union[Unset, bool]):
        mailing_street_address_1 (Union[Unset, str]):
        mailing_street_address_2 (Union[Unset, str]):
        mailing_city (Union[Unset, str]):
        mailing_state (Union[Unset, str]):
        mailing_post_code (Union[Unset, str]):
        mailing_country (Union[Unset, str]):
    """

    user_id: int
    first_name: str
    last_name: str
    street_address_1: str
    city: str
    country: str
    phone: str
    id: Union[Unset, int] = UNSET
    street_address_2: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    mailing_is_different: Union[Unset, bool] = UNSET
    mailing_street_address_1: Union[Unset, str] = UNSET
    mailing_street_address_2: Union[Unset, str] = UNSET
    mailing_city: Union[Unset, str] = UNSET
    mailing_state: Union[Unset, str] = UNSET
    mailing_post_code: Union[Unset, str] = UNSET
    mailing_country: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        first_name = self.first_name
        last_name = self.last_name
        street_address_1 = self.street_address_1
        city = self.city
        country = self.country
        phone = self.phone
        id = self.id
        street_address_2 = self.street_address_2
        state = self.state
        post_code = self.post_code
        mailing_is_different = self.mailing_is_different
        mailing_street_address_1 = self.mailing_street_address_1
        mailing_street_address_2 = self.mailing_street_address_2
        mailing_city = self.mailing_city
        mailing_state = self.mailing_state
        mailing_post_code = self.mailing_post_code
        mailing_country = self.mailing_country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "firstName": first_name,
                "lastName": last_name,
                "streetAddress1": street_address_1,
                "city": city,
                "country": country,
                "phone": phone,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if street_address_2 is not UNSET:
            field_dict["streetAddress2"] = street_address_2
        if state is not UNSET:
            field_dict["state"] = state
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if mailing_is_different is not UNSET:
            field_dict["mailingIsDifferent"] = mailing_is_different
        if mailing_street_address_1 is not UNSET:
            field_dict["mailingStreetAddress1"] = mailing_street_address_1
        if mailing_street_address_2 is not UNSET:
            field_dict["mailingStreetAddress2"] = mailing_street_address_2
        if mailing_city is not UNSET:
            field_dict["mailingCity"] = mailing_city
        if mailing_state is not UNSET:
            field_dict["mailingState"] = mailing_state
        if mailing_post_code is not UNSET:
            field_dict["mailingPostCode"] = mailing_post_code
        if mailing_country is not UNSET:
            field_dict["mailingCountry"] = mailing_country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        street_address_1 = d.pop("streetAddress1")

        city = d.pop("city")

        country = d.pop("country")

        phone = d.pop("phone")

        id = d.pop("id", UNSET)

        street_address_2 = d.pop("streetAddress2", UNSET)

        state = d.pop("state", UNSET)

        post_code = d.pop("postCode", UNSET)

        mailing_is_different = d.pop("mailingIsDifferent", UNSET)

        mailing_street_address_1 = d.pop("mailingStreetAddress1", UNSET)

        mailing_street_address_2 = d.pop("mailingStreetAddress2", UNSET)

        mailing_city = d.pop("mailingCity", UNSET)

        mailing_state = d.pop("mailingState", UNSET)

        mailing_post_code = d.pop("mailingPostCode", UNSET)

        mailing_country = d.pop("mailingCountry", UNSET)

        contact_info = cls(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            street_address_1=street_address_1,
            city=city,
            country=country,
            phone=phone,
            id=id,
            street_address_2=street_address_2,
            state=state,
            post_code=post_code,
            mailing_is_different=mailing_is_different,
            mailing_street_address_1=mailing_street_address_1,
            mailing_street_address_2=mailing_street_address_2,
            mailing_city=mailing_city,
            mailing_state=mailing_state,
            mailing_post_code=mailing_post_code,
            mailing_country=mailing_country,
        )

        contact_info.additional_properties = d
        return contact_info

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
