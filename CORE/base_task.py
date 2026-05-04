# BASE TASK ABSTRACTION

from abc import ABC, abstractmethod

from CORE.result import TaskResult # this line of code here is what "execute should return".

class BaseTask(ABC):
    
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def execute(self, context):
        pass

"""
BaseTask is complete enough to:
    enforce structure
    support all tasks
    work with the pipeline
"""