import pytest
import numpy as np

a_np = np.ones((3, 3), dtype=np.double)
b_np = np.ones((3, 3), dtype=np.double)
c_np = np.ones((3, 3), dtype=np.double)
expected_np = np.array([[4,4,4],[4,4,4],[4,4,4]])

def dgemm_numpy(a, b, c):
  N = a.shape[0]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        c[i][j] = c[i][j] + a[i][k] * b[k][j]
  return c


def test_dgemm():
  assert np.array_equal(dgemm_numpy(a_np,b_np,c_np), expected_np) == True