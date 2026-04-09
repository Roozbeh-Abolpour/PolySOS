import cvxpy as cp
from polysos.algebra.monomial import Monomial
from polysos.moments.moment_matrix import moment_matrix
from polysos.moments.moment_matrix import localizing_matrix
from polysos.moments.multiindex import multiindex

class sos_relaxation:
    def __init__(self, pc, ps, d):
        n=pc.n
        G=multiindex(n,2*d)
        self.y=cp.Variable(len(G))
        self.pc=pc
        self.ps=ps
        self.d=d
        self.G=G
        self.n=n
        self.M=moment_matrix(self.y,G)
        self.Ms=list()
        for p in ps:
            self.Ms.append(localizing_matrix(self.y,p,G))
        self.c=[pc.coefficient(Monomial(alpha)) for alpha in G]