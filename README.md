# Universal Task Runner — V1

## 📌 Overview
A lightweight workflow engine that executes tasks sequentially with controlled failure handling and shared context.

---

## ⚙️ Features (V1)
- Execute shell commands as tasks
- Sequential pipeline execution
- Structured result handling (success / failure)
- Safe error capture (no crashes)
- Shared context between tasks
- Clean, readable output
- Execute Python functions as tasks (V1.1)
---

## 🧠 Architecture
The system is built with clear separation of concerns:

- **Core** → contracts (TaskResult, BaseTask)
- **Tasks** → concrete implementations (ShellTask)
- **Workflow** → execution engine (PipelineRunner)
- **Main** → entry point

## 🧠 Updated Architecture

```text
UNIVERSAL_TASK_RUNNER_V1/
│
├── CORE/
│   ├── result.py
│   ├── base_task.py
│   │
│   ├── tasks/
│   │   ├── shell_task.py
│   │   ├── python_task.py
│   │   │
│   │   └── WORKFLOW/
│   │       └── pipeline.py
│
├── main.py
├── README.md
├── pseudocode.txt
├── breakdown_engine.md
├── requirements.txt
└── .gitignore
```

### Architecture Layers

| Layer | Responsibility |
|---|---|
| `result.py` | Defines structured task outcomes |
| `base_task.py` | Defines the task execution contract |
| `shell_task.py` | Executes terminal commands safely |
| `python_task.py` | Executes Python functions as tasks |
| `pipeline.py` | Controls execution flow and shared context |
| `main.py` | Orchestrates the entire system |
| `pseudocode.txt` | Planning and workflow reasoning |
| `breakdown_engine.md` | Deep engineering dissection and debugging cognition |

---
## 🔧 Tech Stack
- Python
- subprocess (system command execution)
- Object-Oriented Design (Abstraction, Contracts, Separation of Concerns)

---

## How It Works
Task → returns TaskResult → PipelineRunner decides next step 

---

## USAGE
## Run the project: 
python main.py

## Example tasks:
List files,
Check Python version,
Handle invalid commands safely.

## Future Improvements
PythonTask (run Python functions)
FileTask (file operations)
ApiTask (HTTP requests)
Logging system
Retry mechanism
Config-based workflows (YAML/JSON)

##  Project Status

V1 — Core execution engine complete and tested.
V1.1 — Added PythonTask support to prove task extensibility.

## Author Notes

This project focuses on building a reliable execution system with clear contracts and predictable behavior.

Future versions will expand task types and workflow capabilities.

## AUTHOR
```text
KHALID ISHOLA ABDULKADIR