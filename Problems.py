import numpy as np



class Problem:
    def __init__(self, m, n, num_sp, q = 10, M = None):

        # initiate the RNG
        self.rng = np.random.default_rng(seed=m+n)

        # Generate (m x n) Matrix.
        self.M = M if M is not None else self.rng.uniform(-q, q, size=(m, n))

        # Generate y vector.
        self.y = self.rng.uniform(-q, q, size=m)

        # Generate starting points.
        self.sp = [self.rng.uniform(-q, q, size=n) for idx in range(num_sp)]


        #self.sp1, self.sp2, self.sp3, self.sp4, self.sp5 = None, None, None, None, None


    def __repr__ (self):
        return f"M: {self.M.shape}, y: {self.y.shape}, num starting points: {len(self.sp)}"



class ProblemSet:


    def __init__(self):
        self.problem_1 = Problem(1, 2, num_sp = 3)
        self.problem_2 = Problem(2, 4, num_sp = 3)
        self.problem_3 = Problem(3, 6, num_sp = 3)
        self.problem_4 = Problem(4, 8, num_sp = 3)
        self.problem_5 = Problem(5, 10, num_sp = 3)
        self.problem_6 = Problem(10, 20, num_sp= 5,
                                 M=np.array([
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
                                ]))


    def __getitem__(self, item: int):
        starting_points = [self.problem_1, self.problem_2, self.problem_3, self.problem_4, self.problem_5, self.problem_6]
        return starting_points[item]