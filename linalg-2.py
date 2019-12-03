import time

import numpy as np
import scipy as sp
import scipy.io as spio
import scipy.sparse as sparse
import scipy.sparse.linalg as splinalg
import scipy.linalg as linalg

A = spio.mmread("fidapm37.mtx")
b = spio.mmread("fidapm37_rhs1.mtx")

print("x = sparse.linalg.spsolve(A, b) -->")
t_start = time.clock()
x = sparse.linalg.spsolve(A, b)
t_end = time.clock()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)

print()
print("x = linalg.solve(A.todense(), b) -->")
t_start = time.clock()
x = linalg.solve(A.todense(), b)
t_end = time.clock()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)

print()
print("x = AA.I * b -->")
AA = A.todense()
t_start = time.clock()
x = AA.I * b
t_end = time.clock()
print("Execution time:  {:.2f}".format(t_end - t_start))
print(x)
