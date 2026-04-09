import numpy as np
from polysos.chordal_graph.ordering import lexbfs
class ChordalGraph:
    def __init__(self,n,p0):
        V=list(range(n))
        E=set()
        for i in range(n):
            S=list(range(i+1,n))
            N=[i]
            for j in S:
                if np.random.rand() < p0:                    
                    N.append(j)
            
            for n1 in N:
                for n2 in N:
                    if n1<n2:
                        E.add((n1,n2))
        self.V=V
        self.E=sorted(E)
        self.cliques=self.maximal_cliques()
    
    def maximal_cliques(self):        
        p=lexbfs(self)
        n=len(p)
        N=[set() for _ in range(n)]
        for e in self.E:
            N[e[0]].add(e[1])
            N[e[1]].add(e[0])
        cliques=set()
        for i in range(n):
            Nc=[j for j in p[i+1:] if j in N[p[i]]]
            Nc.append(p[i])
            cliques.add(frozenset(Nc))      
        cliques_temp=cliques.copy()  
        for c1 in cliques_temp:
            for c2 in cliques_temp:
                if c1!=c2 and c1.issubset(c2):
                    cliques.remove(c1)
                    break            
        return cliques