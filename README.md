# Python Testing for Research

A (hopefully) beginner-friendly workshop about Python testing tailored to academic and research code. 
The workshop will be held at [DACH+ Linz](https://energy-informatics2026.org/) and [OpenMod Freiburg 2026](https://forum.openmod.org/t/openmod-workshop-freiburg-2026-schedule-program/5955).

## Setup

1. Fork this repo
2. Clone your fork
3. Recommended: Create a virtual Python or conda environment (and activate it)
4. Install package with `python -m pip install -e .` (don't forget the `-e`: it is important!)
5. Test the installation with `python -m pytest tests` in the project root. If you see passing tests you are good to go ;-)

## Example Simulation

Run the PV self-consumption example with:

`python -m python_testing_research.simulation`
