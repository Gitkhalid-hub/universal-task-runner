# Concrete Task (Example: Shell Task)
import subprocess
from CORE.base_task import BaseTask
from CORE.result import TaskResult


class ShellTask(BaseTask):

    def __init__(self, name, command):
        super().__init__(name)
        self.command = command

    def execute(self, context):
        try:
            result = subprocess.run(
                self.command,
                shell=True,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return TaskResult.failure(error=result.stderr)

            return TaskResult.success(data=result.stdout)

        except Exception as e:
            return TaskResult.failure(error=e)
        
"""
ShellTask runs a shell (terminal) command.

It is responsible for:
    executing a command in the system shell
    capturing output on success
    capturing error on failure

Rules:
    must return TaskResult
    must not crash the system
    must convert all errors into failure results

This ensures:
    safe execution of system commands
    consistent result handling in the pipeline
"""