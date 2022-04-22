from enum import Enum


class CommandCommandStatus(str, Enum):
    ATEXECUTION = "AtExecution"
    EXECUTIONREJECTED = "ExecutionRejected"
    EXECUTIONSTOPPED = "ExecutionStopped"
    EXECUTIONSUSPENDED = "ExecutionSuspended"
    ONHOLD = "OnHold"
    PENDING = "Pending"
    PENDINGEXECUTION = "PendingExecution"
    REPLACED = "Replaced"
    RISKPASSED = "RiskPassed"
    RISKREJECTED = "RiskRejected"

    def __str__(self) -> str:
        return str(self.value)
