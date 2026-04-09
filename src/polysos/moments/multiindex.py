
def multiindex(n, d):
    t=[0]*n
    cs=0
    multiindices=list()
    while True:
        multiindices.append(tuple(t.copy()))
        i=n-1
        while i>=0:
            t[i]+=1
            cs+=1
            if cs<=d:
                break
            cs-=t[i]
            t[i]=0
            i-=1
        if i<0:
            break
    
    return multiindices