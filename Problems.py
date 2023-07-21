import numpy as np



class Problem:
    def __init__(self, M, y, sp1, sp2, sp3, sp4=None, sp5=None):
        self.M = M
        self.y = y
        self.sp1 = sp1
        self.sp2 = sp2
        self.sp3 = sp3
        self.sp4 = sp4
        self.sp5 = sp5

    def __repr__ (self):
        counter = 0
        for _ in [self.sp1, self.sp2, self.sp3, self.sp4, self.sp5]:
            if str(_) != "None":
                counter += 1
        return f"M: {self.M.shape}, y: {self.y.shape}, num starting points: {counter}"


def generate_problem(m, n, q=10, num_starting_points=5):
    rng = np.random.default_rng(seed=m+n)

    # Generate (m x n) Matrix.
    M = rng.uniform(-q, q, size=(m, n))

    # Generate y vector.
    y = rng.uniform(-q, q, size=m)

    # Generate starting points.
    sp = [rng.uniform(-q, q, size=n) for idx in range(num_starting_points)]

    return Problem(M, y, *sp)

def _init_problem_6():
    M = np.array([
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
    ])

    problem_6 = generate_problem(10, 20, num_starting_points=5)

    # Replace the randomly generated M with the specified matrix M.
    problem_6.M = M

    # Initialize the Problem
    return problem_6

class ProblemSet:
    def __init__(self):
        self.problem_1 = generate_problem(1, 2)
        self.problem_2 = generate_problem(2, 4)
        self.problem_3 = generate_problem(3, 6)
        self.problem_4 = generate_problem(4, 8)
        self.problem_5 = generate_problem(5, 10)
        self.problem_6 = _init_problem_6()

    def __getitem__(self, item: int):
        problems = [self.problem_1, self.problem_2, self.problem_3, self.problem_4, self.problem_5, self.problem_6]
        return problems[item]