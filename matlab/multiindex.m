function [G,G_index]=multiindex(n,d)
G=[];
t=zeros(1,n);
while 1==1
    G=[G;t];
    i=n;
    while i>=1
        t(i)=t(i)+1;
        if sum(t)<=d
            break
        end
        t(i)=0;
        i=i-1;
    end
    if i<1
        break
    end
end
G_index=containers.Map();
for k = 1:size(G,1)
    G_index(mat2str(G(k,:))) = k;
end
end