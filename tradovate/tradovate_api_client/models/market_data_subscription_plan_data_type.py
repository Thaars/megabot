from enum import Enum


class MarketDataSubscriptionPlanDataType(str, Enum):
    DOM = "DOM"
    TOP = "Top"

    def __str__(self) -> str:
        return str(self.value)
