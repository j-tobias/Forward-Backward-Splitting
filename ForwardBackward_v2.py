
import numpy as np


class ForwardBackward:

    def __init__(self, x, M, y, tau) -> None:
        
        self.M = M          # M denotes the implementation matrix H
        self.x = x          # x denotes the starting Point
        self.stepsize = 0.5 # stepsize determines the distance between the current point and the newly chosen one
        