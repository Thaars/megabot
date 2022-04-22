from enum import Enum


class ExecutionReportExecType(str, Enum):
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    DONEFORDAY = "DoneForDay"
    EXPIRED = "Expired"
    NEW = "New"
    ORDERSTATUS = "OrderStatus"
    PENDINGCANCEL = "PendingCancel"
    PENDINGNEW = "PendingNew"
    PENDINGREPLACE = "PendingReplace"
    REJECTED = "Rejected"
    REPLACED = "Replaced"
    STOPPED = "Stopped"
    SUSPENDED = "Suspended"
    TRADE = "Trade"
    TRADECANCEL = "TradeCancel"
    TRADECORRECT = "TradeCorrect"

    def __str__(self) -> str:
        return str(self.value)
