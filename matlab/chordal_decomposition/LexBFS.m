function p=LexBFS(V,E)
% This function employs teh LEXBFS algrotin to find the
% PEO (Perfect Elimination Ordering) of a chordal graph, required to simply 
% obtain the maximum cliques.
n=length(V);
N=cell(1,n);
for i=1:n
    N{i}=[];
end
for i=1:size(E,1)
    N{E(i,1)}=[N{E(i,1)} E(i,2)]; 
    N{E(i,2)}=[N{E(i,2)} E(i,1)];
end
S=cell(1,n);
for i=1:n
    S{i}=[];
end
p=[];visited=[];
it=n;
while length(p)<n
    I=setdiff(1:n,visited);
    Se=S;Se(visited)=[];
    J=LexLargest(Se);v=I(J);    
    p=[p v];visited=[visited v];
    for i=1:length(N{v})
        u=N{v}(i);
        if isempty(find(visited==u))
            S{u}=[it S{u}];
        end
    end
    it=it-1;
end
end