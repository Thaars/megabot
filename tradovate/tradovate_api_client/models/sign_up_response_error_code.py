from enum import Enum


class SignUpResponseErrorCode(str, Enum):
    DATAERROR = "DataError"
    EMAILALREADYREGISTERED = "EmailAlreadyRegistered"
    EMAILPOLICYFAILED = "EmailPolicyFailed"
    FAILEDRECAPTCHA = "FailedRecaptcha"
    SUCCESS = "Success"
    UNKNOWNERROR = "UnknownError"
    USERALREADYEXISTS = "UserAlreadyExists"
    WEAKPASSWORD = "WeakPassword"
    WRONGCHALLENGE = "WrongChallenge"
    WRONGCHALLENGEORIGIN = "WrongChallengeOrigin"

    def __str__(self) -> str:
        return str(self.value)
