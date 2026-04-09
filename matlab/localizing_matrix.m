function M=localizing_matrix(y,p,G,G_index)
dd=max(sum(G.'));
n=size(G,2);
d=floor(dd/2);
dp=0;
for i=1:size(p,1)
    dp=max(dp,sum(p(i,1:end-1)));
end
if mod(dp,2)==1
    d=d-(floor(dp/2)+1);
else
    d=d-floor(dp/2);
end
Gb=multiindex(n,d);
ngb=size(Gb,1);
M=sdpvar(ngb,ngb,'symmetric');
for i=1:ngb
    for j=i:ngb
        term=0;
        for k=1:size(p,1)
            coeff=p(k,end);powers=p(k,1:end-1);
            gamma=Gb(i,:)+Gb(j,:)+powers;
            ind=G_index(mat2str(gamma));            
            term=term+coeff*y(ind);                        
        end
        M(i,j)=term;
        M(j,i)=term;
    end
end
end