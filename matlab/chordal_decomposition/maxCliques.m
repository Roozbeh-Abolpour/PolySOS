function C=maxCliques(V,E)
% This function finds the maximum cliques of a chordal graph
% represented by (V,E)
n=length(V);
N=cell(1,n);
for i=1:n
    N{i}=[];
end
for i=1:size(E,1)    
    N{E(i,1)}=[N{E(i,1)} E(i,2)]; 
    N{E(i,2)}=[N{E(i,2)} E(i,1)];
end
p=LexBFS(V,E);
C=cell(1,n);
for i=1:n
    Np=intersect(N{p(i)},p(i+1:end));
    C{i}=[p(i) Np];
end
indr=[];
for i=1:n
    for j=i+1:n
        ki=length(intersect(C{i},C{j}));
        if ki==length(C{j})
            indr=[indr j];
            break
        end
    end
end
C(indr)=[];
end