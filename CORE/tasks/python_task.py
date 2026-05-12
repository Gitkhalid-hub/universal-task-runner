# PYTHON TASK: Running a Python function as a task

from CORE.base_task import BaseTask
from CORE.result import TaskResult

class PythonTask(BaseTask):
	
	def __init__(self, name, function):
		super().__init__(name)
		self.function = function
		
	def execute(self, context):
		try:
			result = self.function()
			return TaskResult.success(result)
		
		except Exception as err:
			return TaskResult.failure(err)