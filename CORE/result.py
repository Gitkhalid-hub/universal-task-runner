# STATUS CONTRACT AND TASK RESULT.
from enum import Enum


class Status(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class TaskResult:
    def __init__(self, status, data=None, error=None):

        # Validation None
        if status is None:
            raise ValueError("Status cannot be None")

        # Type Validation
        if not isinstance(status, Status):
            raise TypeError("status must be an instance of Status")

        #Enforce valid combinations
        if status == Status.SUCCESS and error is not None:
            raise ValueError("SUCCESS result cannot have an error")

        if status == Status.FAILURE and error is None:
            raise ValueError("FAILURE result must have an error")

        # Store as private (immutable style)
        self._status = status
        self._data = data
        self._error = error

    #Read-only properties
    @property
    def status(self):
        return self._status

    @property
    def data(self):
        return self._data

    @property
    def error(self):
        return self._error

    # ✅ Helper constructors
    @classmethod
    def success(cls, data=None):
        return cls(Status.SUCCESS, data=data)

    @classmethod
    def failure(cls, error):
        return cls(Status.FAILURE, error=error)
    
"""
TaskResult defines the outcome of every task.

It is used to:
    communicate success or failure
    pass data between tasks
    carry error information when something fails

Rules:
    status must be SUCCESS or FAILURE
    SUCCESS cannot have error
    FAILURE must have error

This ensures:
    predictable pipeline behavior
    no ambiguous states
    safe system execution
"""