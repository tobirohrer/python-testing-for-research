# Repository Guide

## Purpose

- This is a beginner testing workshop built around a battery and a PV self-consumption simulation. Keep the model intentionally simple; exercise scaffolding and incomplete presentation snippets may be deliberate.

## Setup And Verification

- Use Python 3.8 or newer and install the package editable: `python -m pip install -e .`.
- Run the suite with `python -m pytest`; pytest is configured to collect only from `tests/`, excluding illustrative snippets under `slides/`.
- Run one test with `python -m pytest tests/test_battery.py::test_charge -q`; replace the node ID as needed.
- Run the PV self-consumption example with `python -m python_testing_research.simulation`.
- There is no repository-configured lint, formatter, type checker, CI workflow, or separate integration suite.

## Code Map And Gotchas

- `python_testing_research/battery.py` contains the unit-test teaching model. `control()` uses negative values for charging and positive values for discharging, clamps at physical limits, and returns the actual signed transfer.
- `SelfConsumptionController.get_battery_control()` returns load minus PV generation. The simulation applies that request to the battery and calculates the remaining grid exchange; negative grid import means export.
- `python_testing_research/simulation.py` generates an hourly load/PV profile and runs it through the real controller and battery. `tests/test_simulation.py` is the completed higher-level workflow example.
- Treat `build/`, `*.egg-info/`, `__pycache__/`, and `.pytest_cache/` as generated artifacts; edit the source package and tests instead.
