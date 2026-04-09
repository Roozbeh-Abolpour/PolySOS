from polysos.algebra.polynomial import Polynomial
from polysos.algebra.monomial import Monomial
from polysos.sos_relaxation.sos_relaxation import sos_relaxation
from polysos.sos_relaxation_solvers.sos_sdp import sos_sdp
from polysos.sos_relaxation_solvers.sos_socp import sos_socp
from polysos.sos_relaxation_solvers.sos_chordal_sdp import sos_chordal_sdp
from polysos.chordal_graph.chordal_graph import ChordalGraph

pc=Polynomial([Monomial((3,0)),Monomial((1,2)),Monomial((0,1))],[2.0,1.0,1.0])

p1=Polynomial([Monomial((0,0)),Monomial((2,0)),Monomial((0,2))],[1.0,-1.0,-1.0])

p2=Polynomial([Monomial((0,0)),Monomial((1,0)),Monomial((0,3)),Monomial((1,1))],[1.0,1.0,-1.0,1.0])

p3=Polynomial([Monomial((0,2)),Monomial((2,0)),Monomial((0,0))],[-1.0,-1.0,1.0])

ps=[p1,p2,p3]

sos_relax=sos_relaxation(pc,ps,2)
value,y=sos_sdp(sos_relax)
print("Optimal value sdp:", value)
print("Optimal y sdp:", y)

value,y=sos_socp(sos_relax)
print("Optimal value socp:", value)
print("Optimal y socp:", y)

p0=0.5
value,y=sos_chordal_sdp(sos_relax,p0)
print("Optimal value chordal sdp:", value)
print("Optimal y chordal sdp:", y)