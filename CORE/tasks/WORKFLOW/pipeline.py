# PIPELINE RUNNER / CORE ENGINE

from CORE.result import TaskResult, Status


class PipelineRunner:
    def __init__(self, tasks_list):
        self.tasks_list = tasks_list
        self.context_dictionary = {}

    def run(self):
        for task in self.tasks_list:
            print("Running:", task.name)

            result = task.execute(self.context_dictionary)

            if result.status == Status.FAILURE:
                print("Task failed:", task.name)
                return result

            self.context_dictionary[task.name] = result.data

        return TaskResult.success(data=self.context_dictionary)
    
"""
PipelineRunner controls task execution.

It is responsible for:
    running tasks in order
    passing shared context to each task
    stopping execution if a task fails
    collecting results from successful tasks

Rules:
    only the runner controls flow
    tasks must return TaskResult
    context stores task outputs using task names

This ensures:
    predictable execution
    controlled failure handling
    clear data flow between tasks
"""