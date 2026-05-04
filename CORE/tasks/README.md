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

---

## 🧠 Architecture
The system is built with clear separation of concerns:

- **Core** → contracts (TaskResult, BaseTask)
- **Tasks** → concrete implementations (ShellTask)
- **Workflow** → execution engine (PipelineRunner)
- **Main** → entry point

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

## Author Notes

This project focuses on building a reliable execution system with clear contracts and predictable behavior.

Future versions will expand task types and workflow capabilities.

## AUTHOR
```text
KHALID ISHOLA ABDULKADIR