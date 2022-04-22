from enum import Enum


class TradovateSubscriptionPlanDurationUnits(str, Enum):
    MONTH = "Month"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
