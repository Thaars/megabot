from enum import Enum


class SpreadDefinitionSpreadType(str, Enum):
    BUNDLE = "Bundle"
    BUNDLESPREAD = "BundleSpread"
    BUTTERFLY = "Butterfly"
    CALENDARSPREAD = "CalendarSpread"
    CONDOR = "Condor"
    CRACK = "Crack"
    DOUBLEBUTTERFLY = "DoubleButterfly"
    GENERAL = "General"
    INTERCOMMODITYSPREAD = "IntercommoditySpread"
    LAGGEDINTERCOMMODITYSPREAD = "LaggedIntercommoditySpread"
    PACK = "Pack"
    PACKBUTTERFLY = "PackButterfly"
    PACKSPREAD = "PackSpread"
    REDUCEDTICKCALENDARSPREAD = "ReducedTickCalendarSpread"
    REVERSEINTERCOMMODITYSPREAD = "ReverseIntercommoditySpread"
    REVERSESPREAD = "ReverseSpread"
    STRIP = "Strip"
    TREASURYINTERCOMMODITYSPREAD = "TreasuryIntercommoditySpread"

    def __str__(self) -> str:
        return str(self.value)
