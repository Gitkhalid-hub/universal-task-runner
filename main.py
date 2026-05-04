# Entry points

from CORE.tasks.shell_task import ShellTask
from CORE.tasks.WORKFLOW.pipeline import PipelineRunner

# CREATE THE tasks
task1 = ShellTask(name="list_files", command="dir")
task2 = ShellTask(name="check_python", command="python --version")

# CREATE THE PIPELINE
pipeline = PipelineRunner([task1, task2])
result = pipeline.run()

print("\n=== PIPELINE RESULT ===")
print("Status:", result.status.name)

if result.error is not None:
    print("\nPipeline failed.")
    print("Error:", result.error)
else:
    print("\nPipeline completed successfully.")
    print("\nTask Outputs:")

    for task_name, output in result.data.items():
        print(f"- {task_name}: OK")