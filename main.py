import numpy as np

from ForwardBackward import FB_splitting
from Problems import *


Problemset = ProblemSet()


for problem in Problemset:
    M = problem.M
    y = problem.y
    for x in [problem.sp1, problem.sp2, problem.sp3, problem.sp4, problem.sp5]:
        fb = FB_splitting(M, y, x, 1)

