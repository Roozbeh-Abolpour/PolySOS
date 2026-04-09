
def lex_largest(S):
    sm=S[0]
    J=0
    for i in range(1,len(S)):
        s=S[i]
        flag=0
        m=min(len(sm),len(s))
        for j in range(m):
            if s[j]>sm[j]:
                J=i
                sm=s
                flag=1
                break
            elif s[j]<sm[j]:
                flag=-1
                break
        if flag==0 and len(s)>len(sm):
            J=i
            sm=s
    return J
    
def lexbfs(chordal_graph):
    V=chordal_graph.V
    E=chordal_graph.E
    n=len(V)
    N=[set() for _ in range(n)]
    for e in E:
        N[e[0]].add(e[1])
        N[e[1]].add(e[0])
        
    S=[list() for _ in range(n)]
    p=[]    
    visited=set()
    it=n
    while len(p)<n:
        I=[i for i in range(n) if i not in visited]
        Se=[S[i] for i in I]            
        J=lex_largest(Se)            
        v=I[J]
        p.append(v)
        visited.add(v)
        for w in N[v]:                
            if w not in visited:
                S[w]=[it]+S[w]
        it-=1
    return p