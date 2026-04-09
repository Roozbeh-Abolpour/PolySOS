import numpy as np
from polysos.moments.multiindex import multiindex

def moment_matrix_from_polynomial(polynomial,degree):
    p=polynomial
    n=p.n
    d=degree
    coeffs={m.powers: c for m,c in p._terms.items() if m.degree<=2*d}
    G=multiindex(n,d)        
    M=np.zeros((len(G),len(G)))
    for i,alpha in enumerate(G):
        for j in range(i,len(G)):
            beta=G[j]
            gamma=tuple(a+b for a,b in zip(alpha,beta))
            v=coeffs.get(gamma,0)
            M[i,j]=v
            M[j,i]=v
    return M


def localizing_matrix_from_polynomial(base_polynomial,localizing_polynomial,degree):
    y=base_polynomial
    s=localizing_polynomial
    n=y.n    
    d=degree
    ds=s.degree
    Gb=multiindex(n,d)
    coeffs_y={m.powers: c for m,c in y._terms.items() if m.degree<=2*d+ds} 
    coeffs_s={m.powers: c for m,c in s._terms.items() if m.degree<=ds} 
    M=np.zeros((len(Gb),len(Gb)))
    for i,alpha in enumerate(Gb):
        for j in range(i,len(Gb)):
            beta=Gb[j]
            for gamma,c in coeffs_s.items():
                kappa=tuple(a+b+c for a,b,c in zip(alpha,beta,gamma))
                M[i,j]+=coeffs_y.get(kappa,0)*c
                M[j,i]=M[i,j]
    return M



def moment_matrix(y,G):
    n=len(G[0])
    dd=max(sum(alpha) for alpha in G)
    d=(int(dd/2)+1) if dd%2 else int(dd/2)   
    Gb=multiindex(n,d)
    ngb=len(Gb)    
    M=[[0 for _ in range(ngb)] for _ in range(ngb)]
    G_index={alpha: i for i,alpha in enumerate(G)}
    for i,alpha in enumerate(Gb):
        for j in range(i,ngb):
            beta=Gb[j]
            gamma=tuple(a+b for a,b in zip(alpha,beta))
            idx=G_index[gamma]
            v=y[idx]
            M[i][j]=v
            M[j][i]=v
    return M


def localizing_matrix(y,p,G):
    n=len(G[0])
    dd=max(sum(alpha) for alpha in G)
    d=(int(dd/2)+1) if dd%2 else int(dd/2)       
    ds=p.degree
    G_index={alpha: i for i,alpha in enumerate(G)}
    Gb=multiindex(n,d-(int(ds/2)+1) if ds%2 else d-int(ds/2))    
    coeffs_p={m.powers: c for m,c in p._terms.items() if m.degree<=ds} 
    ngb=len(Gb)
    M=[[0 for _ in range(ngb)] for _ in range(ngb)]
    for i,alpha in enumerate(Gb):
        for j in range(i,ngb):
            beta=Gb[j]
            for gamma,coeff in coeffs_p.items():
                kappa=tuple(a+b+c for a,b,c in zip(alpha,beta,gamma))
                idx=G_index[kappa]
                v=y[idx]
                M[i][j]+=v*coeff
                M[j][i]=M[i][j]
    return M
