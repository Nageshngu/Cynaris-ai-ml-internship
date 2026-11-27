# Cynaris AI/ML Internship — Multi-Agent System with CrewAI

## Project overview

Week 1 foundation work for a proposed multi-agent research workflow built with CrewAI. The proposed specialist roles are Researcher, Writer, and Reviewer. **The current scripts explore the folder structure and load sample CSV data; they do not execute CrewAI agents yet.**

## Setup (Windows PowerShell)

Use Python 3.12 for this environment:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify CrewAI after installation:

```powershell
python -c "import crewai; print('CrewAI', crewai.__version__)"
```

## Week 1 Day 1 — Foundation

- Prepare Python and an isolated virtual environment.
- Install CrewAI and CrewAI Tools, and verify installation.
- Initialize a Git repository and document setup notes.
- Do not commit `venv/` or secrets.

## Week 1 Day 2 — Explore codebase structure

Run:

```powershell
python main.py
```

Files and folders:

| Path | Purpose |
| --- | --- |
| `main.py` | Lists project folders, files, and Python file count |
| `data_loader.py` | Loads, previews, and inspects the sample dataset |
| `data/sample_dataset.csv` | Synthetic research briefs for proposed agents |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes environments and secrets |
| `README.md` | Setup notes and data-flow documentation |

CrewAI concepts: agents have **roles** and **goals**, tasks define expected work, and a **Crew** orchestrates task execution. Inter-agent delegation requires explicit configuration.

## Week 1 Day 3 — Map data flow

**Input:** research brief and optional sample CSV data. **Processing:** load and validate the data, then (in the proposed future multi-agent implementation) orchestrate Researcher, Writer and Reviewer tasks. **Output:** a reviewed research report.

```text
+--------------------------+
| User Input / CSV Dataset |
+-------------+------------+
              |
              v
+--------------------------+
| Data Loading & Inspection|
+-------------+------------+
              |
              v
+--------------------------+
| CrewAI Orchestrator      |
| (planned)                |
+-------------+------------+
              |
              v
+--------------------------+
| Researcher Agent         |
| (planned)                |
+-------------+------------+
              |
              v
+--------------------------+
| Writer Agent (planned)   |
+-------------+------------+
              |
              v
+--------------------------+
| Reviewer Agent (planned) |
+-------------+------------+
              |
              v
+--------------------------+
| Reviewed Report (planned)|
+--------------------------+
```

The diagram describes the **target architecture**, not the current executable program.

## Week 1 Day 4 — Load sample data

The synthetic CSV contains 5 research briefs and 5 columns: `task_id`, `topic`, `description`, `agents`, `priority`.

Run:

```powershell
python data_loader.py
```

The loader displays row and column counts, column names and data types, the first five rows, missing values, duplicate rows, and priority counts. For the supplied sample data the expected counts are 5 rows, 5 columns, 0 missing cells and 0 duplicate rows.

## Next steps

Integrate the dataset with configured CrewAI agents and verify an end-to-end multi-agent execution. Save actual terminal screenshots as evidence when the code has been run locally.
