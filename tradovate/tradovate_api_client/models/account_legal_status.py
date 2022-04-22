from enum import Enum


class AccountLegalStatus(str, Enum):
    CORPORATION = "Corporation"
    GP = "GP"
    IRA = "IRA"
    INDIVIDUAL = "Individual"
    JOINT = "Joint"
    LLC = "LLC"
    LLP = "LLP"
    LP = "LP"
    TRUST = "Trust"

    def __str__(self) -> str:
        return str(self.value)
