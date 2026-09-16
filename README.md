# Python Testing for Research

A (hopefully) beginner-friendly workshop about Python testing tailored to academic and research code. 
The workshop will be held at [DACH+ Linz](https://energy-informatics2026.org/) and [OpenMod Freiburg 2026](https://forum.openmod.org/t/openmod-workshop-freiburg-2026-schedule-program/5955).

## Code Overview

The repository contains a small example simulation in which a battery stores surplus PV energy and supplies it later when the PV system does not generate enough electricity to cover the load.

- `python_testing_research/battery.py` contains the battery model. It handles charging and discharging the battery without exceeding it's limits.
- `python_testing_research/controller.py` defines the self-consumption controller. It requests charging the battery when there is excess PV generation and discharging when the load is higher than PV generation.
- `python_testing_research/simulation.py` creates a sample load and PV profile and runs a time step simulation of the battery.
- `tests/` this is where the workshop exercises take place.

## Setup and Preparation

1. Fork this repo
2. Clone your fork
3. Recommended: Create a virtual Python or conda environment (and activate it)
4. Install package with `python -m pip install -e .` (don't forget the `-e`: it is important!)
5. Test the installation with `python -m pytest tests` in the project root. If you see passing tests you are good to go ;-)
6. Run the simulation with `python -m python_testing_research.simulation` (or run `simulation.py` within your IDE). Also, spend a few minutes reviewing `simulation.py` and `battery.py`. You do not need to understand every detail, but familiarizing yourself with the code beforehand will make your life easier during the workshop and allow you to focus on the testing concepts introduced there.
