import cvxpy as cp
from polysos.algebra.polynomial import Polynomial
from polysos.algebra.monomial import Monomial
from polysos.moments.moment_matrix import moment_matrix
from polysos.moments.moment_matrix import localizing_matrix
from polysos.moments.multiindex import multiindex

def sos_socp(sos_relax):
    y=sos_relax.y
    M=sos_relax.M
    Ms=sos_relax.Ms
    c=sos_relax.c
    constraints=[y[0] == 1]
    ne=len(M)
    for i in range(ne):
        for j in range(i+1,ne):
            m1=M[i][i]
            m2=M[i][j]
            m3=M[j][j]
            Q=cp.bmat([[m1,m2],[m2,m3]])
            constraints.append(Q >> 0)            
    for Me in Ms:
        ne=len(Me)
        for i in range(ne):
            for j in range(i+1,ne):
                m1=Me[i][i]
                m2=Me[i][j]
                m3=Me[j][j]
                Q=cp.bmat([[m1,m2],[m2,m3]])
                constraints.append(Q >> 0)  
    objective=cp.Minimize(c@y)
    prob=cp.Problem(objective,constraints)
    prob.solve()
    return prob.value, y.value