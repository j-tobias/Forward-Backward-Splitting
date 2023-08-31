
import numpy as np
from gradient import gradient as GradObjective




def ProximalOperator (x,tau):
    y = np.sign(x)
    y[y > tau] = tau
    y[y < -tau] = -tau
    y = y - tau * np.maximum(np.abs(x) - tau, 0)
    return y
    

class FB_splitting:

    def __init__(self, M, y, x, tau, stepsize = 1.0):
        self.M = M
        self.y = y
        self.x = x
        self.tau = tau
        self.stepsize = stepsize

    def forward (self):
        """
        The Forward Step moves x into the direction of the gradient of the Objective
        """
        gradient = GradObjective(self.x, self.M, self.y, self.tau)
        x_k1 = self.x - self.stepsize * gradient
        return x_k1
    
    def backward (self, x_k1):
        """
        The Backward Step moves the new x into the direction of Proximal Operator
        """
        return ProximalOperator(x_k1, self.tau)

    
    def solve (self, n_iterations = 1000, tol =1e-6):
        """
        Performs the Forward and Backward steps iteravely until the limit of iterations is reached
        """
        steps = []

        for i in range(n_iterations):

            steps.append(self.x)
        
            x_k1 = self.forward()
            x_k1 = self.backward(x_k1)

            distance = np.linalg.norm(self.x - x_k1)


            if distance < tol:
                break
            
            self.x = x_k1
        
        return self.x, np.asarray(steps)