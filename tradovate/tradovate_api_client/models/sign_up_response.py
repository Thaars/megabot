from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sign_up_response_error_code import SignUpResponseErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignUpResponse")


@attr.s(auto_attribs=True)
class SignUpResponse:
    """
    Attributes:
        error_code (SignUpResponseErrorCode): DataError, EmailAlreadyRegistered, EmailPolicyFailed, FailedRecaptcha,
            Success, UnknownError, UserAlreadyExists, WeakPassword, WrongChallenge, WrongChallengeOrigin
        email_verified (bool):
        error_text (Union[Unset, str]): Non-empty if the request failed
        user_id (Union[Unset, int]):
    """

    error_code: SignUpResponseErrorCode
    email_verified: bool
    error_text: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code.value

        email_verified = self.email_verified
        error_text = self.error_text
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorCode": error_code,
                "emailVerified": email_verified,
            }
        )
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_code = SignUpResponseErrorCode(d.pop("errorCode"))

        email_verified = d.pop("emailVerified")

        error_text = d.pop("errorText", UNSET)

        user_id = d.pop("userId", UNSET)

        sign_up_response = cls(
            error_code=error_code,
            email_verified=email_verified,
            error_text=error_text,
            user_id=user_id,
        )

        sign_up_response.additional_properties = d
        return sign_up_response

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
