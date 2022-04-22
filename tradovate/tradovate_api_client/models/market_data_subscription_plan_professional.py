from enum import Enum


class MarketDataSubscriptionPlanProfessional(str, Enum):
    EITHER = "Either"
    NONPROFESSIONAL = "NonProfessional"
    PROFESSIONAL = "Professional"

    def __str__(self) -> str:
        return str(self.value)
