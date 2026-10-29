import numpy as np
from numpy.linalg import inv
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X=np.array(X)
	y=np.array(y)
	thetha= inv(np.transpose(X)@ X)@(np.transpose(X)@ y)
	return thetha