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

Yuri LAVINAS

<!--s-->

### Stochastic Optimization

+ Search methods which use random variables to optimize on an objective function
+ No requirements for the objective function: not differentiable, convex, concave, simple. Any function works.
+ This is not problems which are stochastic (stochastic programming)
+ Other names: metaheuristics, black-box optimization, stochastic search
+ Examples: simulated annealing, particle swarm optimization, evolutionary strategies, genetic algorithms

<!--s-->

### How do they work?

Given a problem and the expected output, how to find a good input (**individual**)?

+ Evaluate several individuals, until we find at least one that works.
    + The fitness function tell how good an individual is.
    + We evaluate how good an individual is by it checking it in the problem in relation to the expected output.
+ Pick the best performing individual
    + Change it a little to get new individuals (**offspring**) and repeat.

<!--s-->

### Why do they work?

+ They work by testing several solutions, until they find a solution that works. They are also called Search Based Optimization (SBO).
+ They don't require domain knowledge or specific characteristic of the problems.
+ These methods are based on random process.
    + Randomness can also make the method less sensitive to modeling errors.
    + Randomness may enable the method to escape a local optimum

<!--s-->

### Why are they great?
<img src="static/img/St_5-xband-antenna.jpg" style="background:none; border:none; box-shadow:none; max-width: 20%; height: auto;"/>

+ "This evolved antenna represents the world's first artificially-evolved object to fly in space."
    + https://en.wikipedia.org/wiki/Evolved_antenna

<!--s-->

### Why are they great?

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">EA for robot control.<a href="https://t.co/VL1bTyOef3">pic.twitter.com/VL1bTyOef3</a></p>&mdash; David Ha (@hardmaru) <a href="https://twitter.com/hardmaru/status/929849328310431744?ref_src=twsrc%5Etfw">November 12, 2017</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

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
  + It is impossible to guarantee they find the optimal individual.

<!--s-->

### Class format

+ Course website at https://SupaeroDataScience.github.io/stochastic/
+ Notebooks available on course website or at https://github.com/SupaeroDataScience/stochastic/
+ Evaluation by quizzes at the end of each class

<!--s-->

### Class schedule

<img src="static/img/schedule.png">

<!--s-->

### Exercise: recent applications

1. [Heuristic Strategies for Solving Complex Interacting Stockpile Blending Problem with Chance Constraints](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/xie_stockpile.pdf)
2. [Design of Specific Primer Sets for SARS-CoV-2 Variants Using Evolutionary Algorithms](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/rincon_cov2.pdf)
3. [Continuously Running Genetic Algorithm for Real-Time Networking Device Optimization](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/mandelbaum_networking.pdf)
4. [Evolutionary Minimization of Traffic Congestion](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/bother_traffic.pdf)
5. [Local Optima Networks for Assisted Seismic History Matching Problems](https://raw.githubusercontent.com/SupaeroDataScience/stochastic/master/articles/seismic_history.pdf)

What is the application in the article? How is this application formulated into an evolutionary fitness?

What is the method used in the article? Describe it in simple terms.
