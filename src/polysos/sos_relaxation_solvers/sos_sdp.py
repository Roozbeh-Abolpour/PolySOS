import cvxpy as cp
from polysos.algebra.polynomial import Polynomial
from polysos.algebra.monomial import Monomial
from polysos.moments.moment_matrix import moment_matrix
from polysos.moments.moment_matrix import localizing_matrix
from polysos.moments.multiindex import multiindex

def sos_sdp(sos_relax):
    y=sos_relax.y
    M=sos_relax.M
    Ms=sos_relax.Ms
    c=sos_relax.c
    constraints=[cp.bmat(M) >> 0]
    constraints.append(y[0] == 1)
    for Me in Ms:
        constraints.append(cp.bmat(Me) >> 0)
    objective=cp.Minimize(c@y)
    prob=cp.Problem(objective,constraints)
    prob.solve()
    return prob.value, y.value