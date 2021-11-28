# Project: Train traffic in Flatland

The [Flatland](https://gitlab.aicrowd.com/flatland/flatland) environment is a 2D
gridworld for developing Multi-Agent Reinforcement Learning. Through simulating
train networks as agents, this platform allows the development of policies for
the efficient management of dense traffic on complex railway networks. We  use
this platform in a project on neuroevolution.

In this project, students compete in teams of their choice of 1-6 people. They
evolve policies for each train in the environment, either using the same genes
for each agent or different genes. Policy representation, stochastic algorithm,
and agent modelling decisions such as inter-agent communication are all up to
the students. Using a fixed budget of evaluations, students must submit their
results and the corresponding code for final evaluation.

This project will take place in class on 01/12. Students are required to install
the Flatland package beforehand and ensure a python environment capable of
running the baseline scripts. Students are encouraged to explore the Flatland
environment before the 01/12. This project coincides with an open competition on
[AIcrowd](https://www.aicrowd.com/challenges/flatland-3) platform with material
prizes. Extra credit will be given to students who make submissions to the
online competition in addition to the class competition.

## Installation

The official installation instructions are
[here](https://gitlab.aicrowd.com/flatland/flatland#-setup). Below are tested
instructions for Linux and the Windows Subsystem for Linux if the official
instructions do not work.

This method was tested on Python 3.7 (WSL) and 3.9 (Linux). You first need a
Python environment which you can install Flatland into. If you already have an
environment, you can **skip this step**. If you want to make a new environment,
this is one way:

```bash
mkdir -p ~/.venvs
python -m venv ~/.venvs/flatland
source ~/.venvs/flatland/bin/activate
pip install -U pip
```

If it is a new environment, or if your environment doesn't have packages like
`numpy` and `pandas` yet, you may need to install Python package building
dependencies:

```bash
pip install wheel cython
```

From a new environment, you should also first install the dependencies from
`requirements_dev.txt`:

```bash
pip install -r requirements_dev.txt
```

Once you have activated a Python environment, you can install the flatland
package:

```bash
git clone git@gitlab.aicrowd.com:flatland/flatland.git
cd flatland
pip install -e .
```


To verify that the installation worked, you can run the package tests:

```bash
pip install pytest
py.test
```

On Linux, you can also see a graphical demonstration by doing

```bash
flatland-demo
```

On Windows Subsystem for Linux, support for graphical display is still underway:
[github](https://github.com/microsoft/WSL/issues/637)
[microsoft](https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps). As
long as you can run the `flatland` package, you are ready for the project.
