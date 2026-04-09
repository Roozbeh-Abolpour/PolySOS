function M=moment_matrix(y,G,G_index)
dd=max(sum(G.'));
n=size(G,2);
d=floor(dd/2);
Gb=multiindex(n,d);
ngb=size(Gb,1);
M=sdpvar(ngb,ngb,'symmetric');
for i=1:ngb
    for j=1:ngb
        gamma=Gb(i,:)+Gb(j,:);
        ind=G_index(mat2str(gamma));
        M(i,j)=y(ind);
        M(j,i)=y(ind);
    end
end
end