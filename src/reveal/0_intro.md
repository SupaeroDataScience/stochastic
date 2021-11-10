---
title: Introduction to Stochastic Optimization
theme: evo
highlightTheme: zenburn
separator: <!--s-->
verticalSeparator: <!--v-->
revealOptions:
    transition: 'fade'
    transitionSpeed: 'default'
    controls: true
    slideNumber: true
    width: '100%'
    height: '100%'
---

## Introduction to Stochastic Optimization

Random Search, Simulated Annealing, Evolutionary Strategies, Genetic Algorithms

**ISAE-SUPAERO, SD**

Dennis WILSON

<!--s-->

### Stochastic Optimization

+ Search methods which use random variables to optimize on an objective function
+ No requirements for the objective function: not differentiable, convex, concave, simple. Any function works.
+ This is not problems which are stochastic (stochastic programming)
+ Other names: metaheuristics, black-box optimization, stochastic search
+ Examples: simulated annealing, particle swarm optimization, evolutionary strategies, genetic algorithms

<!--s-->
### Search: the Traveling Salesman example

<img src="static/img/48StatesTSP.png" style="background:none; border:none; box-shadow:none;"/>

Given a list of cities and the distances between each pair of cities, what is
the shortest possible route that visits each city once and returns to the
origin city?

Representation: list of cities in order

Objective function: total distance traveled

<!--s-->

### Search: Continuous Optimization

<img src="static/img/sgd.gif" style="background:none; border:none; box-shadow:none;"/>

Representation: coordinates in N dimensional space

Objective function: problem-specific

<!--s-->

### Application: wind farm layout optimization

<img src="static/img/LayoutProblem.png" style="background:none; border:none; box-shadow:none;"/>

Representation: x,y coordinates of wind turbines

Objective function: Expected energy gain

Stochastic search methods are state-of-the-art because resolution methods based
on constraint satisfaction or planning are too costly given the physical
simulation of wind turbine wakes.

<!--s-->

### Application: Software development

<img src="static/img/genetic_improvement.png" style="background:none; border:none; box-shadow:none;"/>

Representation: Computer program (grammar or abstract syntax tree)

Objective function: Runtime, number of tests passed


<!--s-->

### Advantages

Pros
  + Flexibility in problem representation
  + Flexibility in objective function
  + Multitude of proven algorithms with (comparatively) few hyperparameters
  + Relatively easy to understand

<!--s-->

### Disadvantages

  + Computational cost
  + Search not fully informed by objective function
  + Expert knowledge for representation or objective function design

<!--s-->

### Class format

+ Course website at https://SupaeroDataScience.github.io/stochastic/
+ Notebooks available on course website or at https://github.com/SupaeroDataScience/stochastic/
+ Evaluation in two parts:
  + mini-quiz on 16/11 and 23/11
  + Project on 01/12

<!--s-->

### Class schedule

<img src="static/img/schedule.png">

<!--s-->

### Exercise: recent applications

1. [Heuristic Strategies for Solving Complex Interacting Stockpile Blending Problem with Chance Constraints](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/xie_stockpile.pdf)
2. [Design of Specific Primer Sets for SARS-CoV-2 Variants Using Evolutionary Algorithms](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/rincon_cov2.pdf)
3. [Continuously Running Genetic Algorithm for Real-Time Networking Device Optimization](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/mandelbaum_networking.pdf)
4. [Evolutionary Minimization of Traffic Congestion](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/bother_traffic.pdf)

What is the application in the article? How is this application formulated into an evolutionary fitness?

What is the method used in the article? Describe it in simple terms.
