---
title: Multi-objective Optimization
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

## Multi-objective Optimization

Pareto dominance, NSGA-II

**ISAE-SUPAERO, SD**

Dennis WILSON

<!--s-->

## Multi-objective Optimization

Optimizing ***more than one** objective function **simultaneously**.

<img src="static/img/tarif_autoroute.jpg" style="background:none; border:none; box-shadow:none;" width="20%" height="auto"/>

+ Multi-objective evolutionary algorithms
+ Pareto dominance
+ NSGA-II
+ Many-objective optimization

<!--s-->

## MOEAs

### Multi-objective evolutionary algorithms

+ **NSGA**: Srinivas, Nidamarthi, and Kalyanmoy Deb. "Muiltiobjective optimization using nondominated sorting in genetic algorithms." Evolutionary computation 2.3 (1994): 221-248.
+ **SPEA2**: Zitzler, Eckart, Marco Laumanns, and Lothar Thiele. "SPEA2: Improving the strength Pareto evolutionary algorithm." TIK-report 103 (2001).
+ **NSGA-II**: Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197.
+ Deb, Kalyanmoy (2001) Multi-objective optimization using evolutionary algorithms. John-Wiley, Chichester
+ **MOEA/D**: Zhang, Qingfu, and Hui Li. "MOEA/D: A multiobjective evolutionary algorithm based on decomposition." IEEE Transactions on evolutionary computation 11.6 (2007): 712-731.
+ Emmerich, Michael TM, and André H. Deutz. "A tutorial on multiobjective optimization: fundamentals and evolutionary methods." Natural computing 17.3 (2018): 585-609. <a href="https://link.springer.com/content/pdf/10.1007/s11047-018-9685-y.pdf">pdf</a>

<!--s-->

## Pareto Dominance

<img src="static/img/pareto_dominance.png" style="background:none; border:none; box-shadow:none;"/>

A solution is said to Pareto dominate another if it is more optimal in all
dimensions.

Solutions which are not dominated by any other are called
"non-dominated".

<!--s-->

## Pareto Front

<img src="static/img/pareto.webp" style="background:none; border:none; box-shadow:none;"/>

The Pareto Front is the set of Pareto Optimal solutions.

In Multi-Objective Optimization, we will search for the Pareto Front.


<!--s-->

## NSGA-II

<img src="static/img/nsgaii.png" style="background:none; border:none; box-shadow:none;" width="50%" height="auto"/>

<small>
Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. <a href="http://repository.ias.ac.in/83498/1/2-a.pdf">pdf</a>
</small>

<!--s-->

## Non-dominated Sorting

<img src="static/img/Diagram-of-nondominated-sorting.png" style="background:none; border:none; box-shadow:none;"/>

<small>
Wang, H. S., C. H. Tu, and K. H. Chen. "Supplier selection and production planning by using guided genetic algorithm and dynamic nondominated sorting genetic algorithm II approaches." Mathematical Problems in Engineering 2015 (2015).
</small>

<!--s-->

## Fast non-dominated sort

<img src="static/img/fast_non_dominated.png" style="background:none; border:none; box-shadow:none;"/>

<small>
Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. <a href="http://repository.ias.ac.in/83498/1/2-a.pdf">pdf</a>
</small>

<!--s-->

## Crowding Distance Assignment

<img src="static/img/crowding_distance.png" style="background:none; border:none; box-shadow:none;"/>

<img src="static/img/crowding_distance_calculation.png" style="background:none; border:none; box-shadow:none;"/>

<small>
Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. <a href="http://repository.ias.ac.in/83498/1/2-a.pdf">pdf</a>
</small>

<!--s-->

## NSGA-II Overview

<img src="static/img/nsgaii.png" style="background:none; border:none; box-shadow:none;" width="40%" height="auto"/>

<img src="static/img/crowding_distance_gr.png" style="background:none; border:none; box-shadow:none;"/>

<small>
Deb, Kalyanmoy, et al. "A fast and elitist multiobjective genetic algorithm: NSGA-II." IEEE transactions on evolutionary computation 6.2 (2002): 182-197. <a href="http://repository.ias.ac.in/83498/1/2-a.pdf">pdf</a>
</small>

<!--s-->

## Problems with Non-Dominance

<img src="static/img/problem_with_pareto.png" style="background:none; border:none; box-shadow:none;"/>

With more objectives, some objectives may be overrepresented in the non-dominated set.

<small>
Ishibuchi, Hisao, and Hiroyuki Sato. "Evolutionary many-objective optimization."
<a href="https://dl.acm.org/doi/proceedings/10.1145/3205651">Proceedings of the Genetic and Evolutionary Computation Conference Companion.</a> 2019.
</small>

<!--s-->

## Many-objective Optimization

<img src="static/img/pareto_num_solutions.png" style="background:none; border:none; box-shadow:none;"/>

When increasing beyond a small number (2-4) of objectives,

the chance of fully non-dominated solutions decreases.

Different algorithms, visualization methods, convergence metrics are needed.

<small>
Ishibuchi, Hisao, and Hiroyuki Sato. "Evolutionary many-objective optimization."
<a href="https://dl.acm.org/doi/proceedings/10.1145/3205651">Proceedings of the Genetic and Evolutionary Computation Conference Companion.</a> 2019.
</small>
