function [y,M,Ms,c]=sos_relaxation(pc,ps,d)
n=size(pc,2)-1;
[G,G_index]=multiindex(n,2*d);
ng=size(G,1);y=sdpvar(ng,1);
M=moment_matrix(y,G,G_index);
np=length(ps);
Ms=cell(1,np);
for i=1:np
    Ms{i}=localizing_matrix(y,ps{i},G,G_index);
end
c=zeros(ng,1);
for i=1:size(pc,1)
    powers=pc(i,1:end-1);coeff=pc(i,end);
    ind=G_index(mat2str(powers));
    c(ind)=coeff;
end
end