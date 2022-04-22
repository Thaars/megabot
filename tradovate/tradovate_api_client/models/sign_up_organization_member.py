from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SignUpOrganizationMember")


@attr.s(auto_attribs=True)
class SignUpOrganizationMember:
    """
    Attributes:
        name (str):
        email (str):
        password (str):
        first_name (str):
        last_name (str):
    """

    name: str
    email: str
    password: str
    first_name: str
    last_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        password = self.password
        first_name = self.first_name
        last_name = self.last_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "password": password,
                "firstName": first_name,
                "lastName": last_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email")

        password = d.pop("password")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        sign_up_organization_member = cls(
            name=name,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        sign_up_organization_member.additional_properties = d
        return sign_up_organization_member

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
