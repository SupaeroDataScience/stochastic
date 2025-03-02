---
title: Introduction to Stochastic Optimization
theme: evo
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

### Evolutionary Algorithms


<img src="static/img/EA_diagram.svg" style="background:none; border:none; box-shadow:none;" width="50%" height="auto"/>

Population of solutions are evaluated, selected, then modified to create the next population.

<!--s-->

### Why do they work?

+ They work by testing several solutions, until they find a solution that works.
+ They don't require domain knowledge or specific characteristic of the problems.
+ These methods are based on random process.
    + Randomness can also make the method less sensitive to modeling errors.
    + Randomness may enable the method to escape a local optimum.

<!--s-->

### Why are they great?

<img src="static/img/St_5-xband-antenna.jpg" style="background:none; border:none; box-shadow:none; max-width: 20%; height: auto;"/>

 "This evolved antenna represents the world's first artificially-evolved object to fly in space."

https://en.wikipedia.org/wiki/Evolved_antenna

<!--s-->

### Why are they great?

<img src="https://blog.otoro.net/assets/20171109/biped/biped_cma.gif" style="background:none; border:none; box-shadow:none; max-width: 80%; height: auto;"/>

Robotic control with evolved logic

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

  + Creative
  + Easy to implement and parallelize
  + Flexibility in problem representation and in fitness function
  + Many proven algorithms with (comparatively) few hyperparameters
  + Relatively easy to understand

<!--s-->

### Disadvantages

  + Computational cost
  + Search not fully informed by fitness function
  + Not guaranteed to find the optimal individual

<!--s-->

### Class format

+ Course website at https://SupaeroDataScience.github.io/stochastic/
+ Notebooks available on course website or at https://github.com/SupaeroDataScience/stochastic/
+ Evaluation by quizzes at the beginning of second and third class

<!--s-->

### Class schedule

Schedule | | |
| --- | --- | --- |
03/03 | [Random search](1_sa.html) | Continuous optimization, random search, simulated annealing |
05/03 | [Evolutionary Strategies](2_es.html) | Population-based methods, 1+1 ES, CMA-ES |
05/03 | [Genetic Algorithms](3_ga.html) | Genetic Algorithm, Multi-Objective Optimization, NSGA-II |

<!--s-->

### Exercise: recent applications

1. [Heuristic Strategies for Solving Complex Interacting Stockpile Blending Problem with Chance Constraints](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/xie_stockpile.pdf)
2. [Design of Specific Primer Sets for SARS-CoV-2 Variants Using Evolutionary Algorithms](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/rincon_cov2.pdf)
3. [Continuously Running Genetic Algorithm for Real-Time Networking Device Optimization](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/mandelbaum_networking.pdf)
4. [Evolutionary Minimization of Traffic Congestion](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/bother_traffic.pdf)
5. [From Pixels to Metal: AI-Empowered Numismatic Art](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/machado_pixels.pdf)
6. [Evolutionary design of explainable algorithms for biomedical image segmentation](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/cortacero_image.pdf)
7. [Freeform generative design of complex functional structures](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/pereira_freeform.pdf)
8. [Learning Traffic Signal Control via Genetic Programming](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/zhang_traffic.pdf)

What is the application in the article? How is this application formulated into an evolutionary fitness?

What is the method used in the article? Describe it in simple terms.
