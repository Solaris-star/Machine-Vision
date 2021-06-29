import numpy as np
a = np.array([[0.866,-0.5,0],
             [0.5,0.866,0],
             [0,0,1]])
b = np.array([[4],[2],[2]])

print(np.dot(a,b))