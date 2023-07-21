import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gradient(x, M, y, tau):
  """Computes the gradient of the given term.

  Args:
    x: A numpy array of shape (2,).
    M: A numpy array of shape (1, 2).
    y: A numpy array of shape (1,).
    tau: A positive scalar.

  Returns:
    A numpy array of shape (2,).
  """

  grad_x1 = tau * (1 / np.linalg.norm(x, ord=1)) * np.sign(x)
  grad_x2 = 0.5 * M.T @ (np.matmul(M, x) - y) / np.linalg.norm(np.matmul(M, x) - y)
  grad_x = grad_x1 + grad_x2
  return grad_x2


def function (x, M, y, tau):
  """Computes the function of the given term.

  Args:
    x: A numpy array of shape (2,).
    M: A numpy array of shape (1, 2).
    y: A numpy array of shape (1,).
    tau: A positive scalar.

  Returns:
    A Float.
  """
  return (0.5 * np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.linalg.norm(x, ord=1))


# OLD VERSIONS - DO NOT USE THEM
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------

def GradObjective (M,x,y,tau):
    """
    returns the gradient of the Objective evaluated with respect to x
    grad f = M * ((M * x) - y) + tau * sign(x)
    """
    grad_x1 = tau * (1 / np.linalg.norm(x, ord=1)) * np.sign(x)
    grad_x2 = 0.5 * M.T @ (np.matmul(M, x) - y) / np.linalg.norm(np.matmul(M, x) - y)
    grad_x = grad_x1 + grad_x2
    return grad_x
    return (M.T @ (np.matmul(M, x) - y) / np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.sign(x))
    return np.matmul(M.T, np.matmul(M, x) - y) + tau * np.sign(x)


def Objective (M,x,y,tau):
    """
    M := m rows and n = 2m
    y := vector y ∈ R^m
    x := vector x ∈ R^n
    tau := positive scalar (1)
    """
    return (0.5 * np.linalg.norm(np.matmul(M, x) - y)) + (tau * np.linalg.norm(x, ord=1))