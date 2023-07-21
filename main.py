import numpy as np

from ForwardBackward import FB_splitting
from Problems import *
from gradient import Objective

Problemset = ProblemSet()

#tau = 3
tau = 0.2
stepsize = 0.3
num_steps = 20000

for problem in Problemset:
    M = problem.M
    y = problem.y
    for x in [problem.sp1, problem.sp2, problem.sp3, problem.sp4, problem.sp5]:

        fb = FB_splitting(M, y, x, tau, stepsize)
        solution, steps = fb.solve(num_steps)

        end = Objective(M, solution, y, tau)
        start = Objective(M, x, y, tau)
        print(30*"__")
        print("Problem size: ", M.shape)
        print("\nStarting point: ", [np.round(_, 3) for _ in x])
        print('Final Point:    ', [np.round(_, 3) for _ in solution])
        print('\nObjective value at starting point: ', np.round(start, decimals=3))
        print('Objective value at final point:    ', np.round(end,   decimals=3))
        print("\nRequired Num Steps: ", len(steps))
