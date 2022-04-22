from enum import Enum


class UserAccountRiskParameterProductVerificationStatus(str, Enum):
    INACTIVE = "Inactive"
    LOCKED = "Locked"
    READYFORCONTRACTS = "ReadyForContracts"
    READYTOTRADE = "ReadyToTrade"
    VERIFIED = "Verified"

    def __str__(self) -> str:
        return str(self.value)
