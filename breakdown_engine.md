# 🧩 Breakdown Engine — Universal Task Runner

> **Technical Detective Lens:** This document dissects each module of the project, highlighting functionality, structure, edge cases, and design patterns.

---

## Module Links

- 🛠️ [TaskResult — `CORE/result.py`](CORE/result.py)
- 🛠️ [BaseTask — `CORE/base_task.py`](CORE/base_task.py)
- 🛠️ [ShellTask — `CORE/tasks/shell_task.py`](CORE/tasks/shell_task.py)
- 🛠️ [PythonTask — `CORE/tasks/python_task.py`](CORE/tasks/python_task.py)
- 🛠️ [PipelineRunner — `CORE/tasks/WORKFLOW/pipeline.py`](CORE/tasks/WORKFLOW/pipeline.py)
- 🛠️ [Orchestration — `main.py`](main.py)

---

## 1️⃣ Surface Behavior

> What does the project output at a glance?

<details>
<summary>Universal Task Runner</summary>

```python
pipeline = PipelineRunner([task1, task2, task3])
result = pipeline.run()
```

This system:

- Creates task objects.
- Runs tasks sequentially.
- Passes shared context into each task.
- Stops the pipeline if any task fails.
- Stores successful task outputs in a context dictionary.
- Returns a structured `TaskResult`.

</details>

---

## 2️⃣ Line-by-Line Behavior

> Inspect each major module for concrete action.

<details>
<summary>TaskResult — Result Contract</summary>

```python
class Status(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
```

Defines the only valid task states.

```python
class TaskResult:
    def __init__(self, status, data=None, error=None):
```

Creates a structured result object.

```python
if status is None:
    raise ValueError("Status cannot be None")
```

Prevents missing status.

```python
if not isinstance(status, Status):
    raise TypeError("status must be an instance of Status")
```

Ensures only valid `Status` enum values are used.

```python
if status == Status.SUCCESS and error is not None:
    raise ValueError("SUCCESS result cannot have an error")
```

Prevents contradictory success states.

```python
if status == Status.FAILURE and error is None:
    raise ValueError("FAILURE result must have an error")
```

Prevents unclear failure states.

```python
@classmethod
def success(cls, data=None):
    return cls(Status.SUCCESS, data=data)
```

Shortcut for successful results.

```python
@classmethod
def failure(cls, error):
    return cls(Status.FAILURE, error=error)
```

Shortcut for failed results.

</details>

<details>
<summary>BaseTask — Abstract Task Contract</summary>

```python
class BaseTask(ABC):
```

Creates an abstract base class.

```python
def __init__(self, name):
    self.name = name
```

Every task must have a name.

```python
@abstractmethod
def execute(self, context):
    pass
```

Forces every task subclass to implement `execute`.

This means every task must follow the same interface:

```text
task.execute(context) → TaskResult
```

</details>

<details>
<summary>ShellTask — Running Terminal Commands</summary>

```python
class ShellTask(BaseTask):
```

Creates a concrete task type based on `BaseTask`.

```python
def __init__(self, name, command):
    super().__init__(name)
    self.command = command
```

Stores the command to run.

```python
result = subprocess.run(
    self.command,
    shell=True,
    capture_output=True,
    text=True
)
```

Runs the command safely and captures output.

```python
if result.returncode != 0:
    return TaskResult.failure(error=result.stderr)
```

If the command fails, return a failure result.

```python
return TaskResult.success(data=result.stdout)
```

If the command succeeds, return output as success data.

```python
except Exception as e:
    return TaskResult.failure(error=e)
```

Any unexpected error becomes a safe failure result.

</details>

<details>
<summary>PythonTask — Running Python Functions</summary>

```python
class PythonTask(BaseTask):
```

Creates a task type for running Python functions.

```python
def __init__(self, name, function):
    super().__init__(name)
    self.function = function
```

Stores the function that should run as a task.

```python
result = self.function(context)
```

Runs the stored Python function using shared pipeline context.

```python
return TaskResult.success(result)
```

Returns the function output as successful task data.

```python
except Exception as err:
    return TaskResult.failure(err)
```

If the function fails, convert the error into a `TaskResult`.

</details>

<details>
<summary>PipelineRunner — Core Execution Engine</summary>

```python
self.tasks_list = tasks_list
self.context_dictionary = {}
```

Stores all tasks and creates shared context.

```python
for task in self.tasks_list:
```

Runs tasks one by one.

```python
result = task.execute(self.context_dictionary)
```

Passes shared context into the current task.

```python
if result.status == Status.FAILURE:
    print("Task failed:", task.name)
    return result
```

Stops execution immediately if a task fails.

```python
self.context_dictionary[task.name] = result.data
```

Stores successful task output using task name as key.

```python
return TaskResult.success(data=self.context_dictionary)
```

Returns the full pipeline context after all tasks succeed.

</details>

---

## 3️⃣ Variable Purpose

<details>
<summary>Important Variables</summary>

| Variable | Purpose |
|---|---|
| `status` | Whether a task succeeded or failed |
| `data` | Successful output from a task |
| `error` | Failure information from a task |
| `name` | Unique task identifier |
| `command` | Shell command executed by `ShellTask` |
| `function` | Python function executed by `PythonTask` |
| `context_dictionary` | Shared memory between pipeline tasks |
| `tasks_list` | Ordered list of tasks to execute |
| `result` | Output object returned by each task |

</details>

---

## 4️⃣ System Flow

<details>
<summary>Main Pipeline Flow</summary>

```text
main.py
↓
create tasks
↓
create PipelineRunner
↓
PipelineRunner.run()
↓
execute task 1
↓
store output in context
↓
execute task 2
↓
store output in context
↓
execute task 3
↓
store output in context
↓
return final TaskResult
```

If any task fails:

```text
task failure
↓
TaskResult.failure
↓
PipelineRunner stops
↓
main.py prints failure
```

</details>

---

## 5️⃣ Edge Cases

<details>
<summary>Possible Failures</summary>

- Shell command does not exist.
- Shell command returns non-zero exit code.
- Python function raises an exception.
- Python function expects context but context is missing a required key.
- Task does not return a valid `TaskResult`.
- A task name is duplicated, causing context overwrite.
- Pipeline receives an empty task list.
- `Status` is passed incorrectly into `TaskResult`.

</details>

---

## 6️⃣ Structural Pattern

<details>
<summary>Contract Pattern</summary>

`BaseTask` defines the contract:

```text
Every task must implement execute(context)
```

This allows the pipeline to treat different task types the same way.

```text
ShellTask
PythonTask
Future FileTask
Future ApiTask
```

All can be executed through:

```python
task.execute(context)
```

</details>

<details>
<summary>Result Object Pattern</summary>

`TaskResult` standardizes task outcomes.

Instead of returning random values, every task returns:

```text
status
data
error
```

This prevents ambiguous pipeline behavior.

</details>

<details>
<summary>Shared Context Pattern</summary>

The pipeline stores each task result in:

```python
context_dictionary[task.name] = result.data
```

This allows later tasks to access earlier task outputs.

</details>

---

## 7️⃣ Reframe / Visualize

<details>
<summary>Pipeline Table</summary>

| Task Name | Task Type | Output Stored As |
|---|---|---|
| `list_files` | ShellTask | `context["list_files"]` |
| `check_python` | ShellTask | `context["check_python"]` |
| `fibonacci` | PythonTask | `context["fibonacci"]` |

</details>

---

## 8️⃣ Project Data Shape

<details>
<summary>Final Context Shape</summary>

```python
{
    "list_files": "...terminal output...",
    "check_python": "...python version...",
    "fibonacci": [0, 1, 1, 2, 3]
}
```

This dictionary represents the final successful pipeline state.

</details>

---

## 9️⃣ Insights & Recommendations

- ✅ `TaskResult` makes system behavior predictable.
- ✅ `BaseTask` enforces task structure.
- ✅ `PipelineRunner` owns execution flow.
- ✅ `ShellTask` and `PythonTask` prove extensibility.
- ✅ Shared context enables task communication.
- ⚠️ `PythonTask` should call `self.function(context)`.
- ⚠️ Duplicate task names can overwrite context data.
- ⚠️ Future versions should add logging and retry support.

---

## ⚡ 8-Step Truth-Finding Approach

Use this when debugging or extending the project:

1. Surface Behavior
2. Line-by-Line Behavior
3. Variable Purpose
4. System Flow
5. Edge Cases
6. Structural Pattern
7. Reframe / Visualize
8. Insights & Recommendations

---

## 🧠 Final Detective Summary

Universal Task Runner is a small workflow engine.

Its core intelligence is not in one task.

Its intelligence comes from:

```text
contract
↓
execution
↓
result validation
↓
shared context
↓
controlled failure handling
```

This project teaches:

- abstraction
- contracts
- orchestration
- safe failure handling
- task extensibility
- pipeline architecture

The key idea:

```text
Different task types can run through the same execution engine
as long as they obey the same TaskResult contract.
```