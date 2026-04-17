import cvxpy as cp
from polysos.algebra.polynomial import Polynomial
from polysos.algebra.monomial import Monomial
from polysos.moments.moment_matrix import moment_matrix
from polysos.moments.moment_matrix import localizing_matrix
from polysos.moments.multiindex import multiindex
from polysos.chordal_graph.chordal_graph import ChordalGraph

def sos_chordal_sdp(sos_relax,p0):
    y=sos_relax.y
    M=sos_relax.M
    Ms=sos_relax.Ms
    c=sos_relax.c
    constraints=[y[0] == 1]
    chordal_graph=ChordalGraph(len(M),p0)
    for clique in chordal_graph.cliques:
            M_clique=[[M[i][j] for j in clique] for i in clique]
            constraints.append(cp.bmat(M_clique) >> 0)
    for Me in Ms:
        chordal_graph=ChordalGraph(len(Me),p0)
        for clique in chordal_graph.cliques:
            Me_clique=[[Me[i][j] for j in clique] for i in clique]
            constraints.append(cp.bmat(Me_clique) >> 0)
    objective=cp.Minimize(c@y)
    prob=cp.Problem(objective,constraints)
    prob.solve()
    if y.value is None:
        raise ValueError(f"Chordal SOS solve failed. Status: {prob.status}")
    return prob.value, y.value
