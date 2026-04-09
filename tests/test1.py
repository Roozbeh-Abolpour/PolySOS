import polysos.moments.multiindex as multiindex
n=8
d=6

G=multiindex.multiindex(n, d)
for g in G:
    print(g)