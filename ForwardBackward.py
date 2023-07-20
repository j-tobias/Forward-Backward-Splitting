
import numpy as np
from tqdm import tqdm

def Objective (M,x,y,tau):
    """
    M := m rows and n = 2m
    y := vector y ∈ R^m
    x := vector x ∈ R^n
    tau := positive scalar (1)
    """
    return (0.5 * np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.linalg.norm(x, ord=1))

def GradObjective (M,x,y,tau):
    """
    returns the gradient of the Objective evaluated with respect to x
    grad f = M * ((M * x) - y) + tau * sign(x)
    """
    return (M.T @ (np.matmul(M, x) - y) / np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.sign(x))
    return np.matmul(M.T, np.matmul(M, x) - y) + tau * np.sign(x)

def ProximalOperator (x,tau):
    #return np.sign(x) * np.maximum(np.abs(x) - tau, 0)
    return np.matmul(np.sign(x), np.maximum(np.abs(x) - tau, 0))
    

class FB_splitting:

    def __init__(self, M, y, x, tau):
        self.M = M
        self.y = y
        self.x = x
        self.tau = tau
        self.stepsize = 1.0


    def forward (self):
        """
        Forward Step: In the forward step, we update the variable x based on the gradient of the differentiable function g(x). The update rule is typically given by:
        x^(k+1) = x^k - α * ∇g(x^k)
        where x^k represents the value of x at iteration k, α is the step size (also known as the learning rate), and ∇g(x^k) denotes the gradient of g(x) evaluated at x^k.
        """
        #x_k1 = self.x - self.stepsize * GradObjective(self.M, self.x, self.y, self.tau)
        gradient = GradObjective(self.M, self.x, self.y, self.tau)
        #x_k1 = tf.subtract(self.x, tf.multiply(self.stepsize, gradient))
        x_k1 = self.x - self.stepsize * gradient
        return x_k1
    
    def backward (self, x):
        return ProximalOperator(x, self.tau)
    
    def solve (self, n_iterations = 1000, tol =1e-6):

        steps = []

        for i in range(n_iterations):

            #print(self.x)
        
            x_k1 = self.forward()
            #x_k1 = self.backward(x_k1)

            if np.linalg.norm(self.x - x_k1) < tol:
                break
            
            self.x = x_k1
            steps.append(x_k1)
            
        
        return self.x, np.asarray(steps)