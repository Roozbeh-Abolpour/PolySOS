function [V,E]=genChordalGraph(n,p0)
% This function genrates a random chordal graph
% V represents its vertices labeled by 1,2,...,n
% E represents its edges such that its rows includes 
%   the connected vertices. For example, 
% E=[2 3;1 4] means v2-v3 and v1-v4 are the edges of the graph  
V=1:n;E=[];
for i=1:n-1
    S=i+1:n;
    p=rand(1,length(S))<p0;
    N=[i S(p)];
    for j=1:length(N)
        for k=j+1:length(N)
            E=[E;N(j) N(k)];
        end
    end
end
E=unique(sort(E,2),'rows');
end