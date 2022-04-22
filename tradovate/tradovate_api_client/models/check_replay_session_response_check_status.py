from enum import Enum


class CheckReplaySessionResponseCheckStatus(str, Enum):
    INELIGIBLE = "Ineligible"
    OK = "OK"
    STARTTIMESTAMPADJUSTED = "StartTimestampAdjusted"

    def __str__(self) -> str:
        return str(self.value)
