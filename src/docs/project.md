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
git clone https://gitlab.aicrowd.com/flatland/flatland
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

## In-class project

During class, we will use evolution to find good agents for trains. Starting
evolution scripts and environments are
[here](https://github.com/SupaeroDataScience/flatland-project). You should clone this repository and work in it, using a flatland environment:

`git clone https://github.com/SupaeroDataScience/flatland-project`

In this folder, there are multiple scripts ready to help with the project:

+ `evaluate.py` : loads railway environments and evaluates a neural network agent by simulating an episode
+ `policy.py` : an agent which controls a train by mapping observations to actions
+ `observation_utils.py` : utility functions to handle observations, taken from the flatland [starter kit](https://gitlab.aicrowd.com/flatland/flatland-starter-kit)
+ `evolution.py` : an example evolution of an agent using a 1+lambda ES
+ `test.py` : a script to run a saved individual on multiple different episodes
+ `random_agent.py` : an example of an episode with random actions at every step which you can use to explore the environment

To run an evolution on the `small` environment for 10 generations, use the
following command:

`python evolution.py --env small --gens 10 --weights example.weights`

This will create two output files: `evolution.log` and `example.weights`. The
final output of this script should be a fitness value (something like -100).
Confirm that the individual was saved by using the following:

`python test.py --env small --weights example.weights`

This should output three fitness values similar to the final value of evolution.
Note that evolution uses the same environment for each evaluation (same random
seed) but the test is based on multiple random seeds. If you want to see the
visual rendering of the environment, you can run (may not work on Windows):

`python test.py --env small --weight example.weights --render True`

## Tasks and evaluation

We will focus on the evolution of solutions for three fixed environments:
`small.pkl`, `medium.pkl`, and `large.pkl`. You will have a budget of 1000
**evaluations** equivalent to the 1+lambda ES for 100 generations with a
population size of 10. For the `small` environment, this should take around 10
minutes on an ordinary laptop.

Your final evaluation will be on the `large.pkl` environment, however this takes
much longer to run so you are advised to develop solutions on the `small.pkl`
environment first.

Your task is to improve the performance of evolution of a solution. You can
explore whichever direction you think is most promising, including but not
limited to:

+ replacing the 1+lambda ES with a different algorithm
+ changing evolutionary hyperparameters like population size and standard deviation
+ modifying the agent [observations](https://flatland.aicrowd.com/environment/observations.html)
+ modifying the policy network
+ changing the fitness function

Your final results on the `large.pkl` environment will be evaluated using three criteria:

+ final result during evolution (fitness at the end of an episode)
+ convergence speed (how quickly the evolution improves)
+ robustness to different random environments (as in `test.py`)

## Resources

You can use any algorithm, including code from class, but the following libraries may be of help:

+ https://github.com/hardmaru/estool
+ https://pymoo.org/
+ https://github.com/CyberAgentAILab/cmaes

## Submission

To submit your results, you should submit all necessary python files, model
weights, and the log file of your evolution by the end of the Sunday
December 12. An example submission is provided in `example_submission`, which
you can copy for your own work:

`cp -r example_submission TEAM_NAME`

In this folder, you **must modify the following files**:

+ `team.txt`, to include the names of all your team members
+ `method.txt`, a **short** (less than 500 character) description of your method.

To submit your solution, you can either upload this folder to the
[LMS](https://lms.isae.fr/mod/assign/view.php?id=85073) or to the github
repository. To submit through github, first fork the
[repository](https://github.com/SupaeroDataScience/flatland-project), then add
your remote:

`git remote add myfork FORK_URL`

Add your results folder, commit, and push to your fork:

```bash
git add TEAM_NAME
git commit -m 'submission'
git push myfork main
```

## Bonus: Flatland competition submission

Bonus points will be awarded to students who compete in the Flatland competition.

If you'd like to participate in the [Flatland
competition](https://www.aicrowd.com/challenges/flatland-3), follow the
instructions in the [Flatland starter
kit](https://gitlab.aicrowd.com/flatland/flatland-starter-kit/). Full instructions are [here](https://gitlab.aicrowd.com/flatland/flatland-starter-kit/-/blob/master/docs/SUBMISSION.md).

It is recommended that you complete a longer evolution than 1000 evaluations for
the public competition, and that you include different environment types. Note that the
provided environments for this project do not include
[malfunctions](https://flatland.aicrowd.com/environment/stochasticity.html) for
simplicity and so models trained on the in-class environments may not work well
in the final evaluation.  To include malfunctions, you must create new
environments.

If you do compete in the Flatland competition, please send me the link of your
position on the leaderboards. Good luck!
