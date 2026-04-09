import numpy as np

from polysos.algebra.monomial import Monomial
from polysos.algebra.polynomial import Polynomial
from polysos.moments.moment_matrix import moment_matrix_from_polynomial
from polysos.moments.moment_matrix import localizing_matrix_from_polynomial

y = Polynomial(
    [
        Monomial((0, 0)),
        Monomial((1, 0)),
        Monomial((0, 1)),
        Monomial((2, 0)),
        Monomial((1, 1)),
        Monomial((0, 2)),
        Monomial((3, 0)),
        Monomial((2, 1)),
        Monomial((1, 2)),
        Monomial((0, 3)),
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)

s = Polynomial(
    [
        Monomial((0, 0)),
        Monomial((1, 0)),
        Monomial((0, 1)),
    ],
    [1, -1, -1]
)

d = 2

M_moment = moment_matrix_from_polynomial(y, d)
M_local = localizing_matrix_from_polynomial(y, s, d)

print("Computed moment matrix:")
print(M_moment)
print()

print("Computed localizing matrix:")
print(M_local)
print()
