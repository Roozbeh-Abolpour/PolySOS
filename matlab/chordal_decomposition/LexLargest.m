function J=LexLargest(S)
% This function finds the lexicographically largest entry of set S
sm=S{1};J=1;
for i=2:length(S)
    s=S{i};flag=0;
    for j=1:min(length(s),length(sm))
        if s(j)>sm(j)
            J=i;sm=s;
            flag=1;
            break
        elseif s(j)<sm(j)
            flag=1;
            break
        end
    end
    if flag==0&&length(s)>length(sm)
        J=i;sm=s;
    end
end
end