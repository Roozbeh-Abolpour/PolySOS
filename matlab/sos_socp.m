function y=sos_socp(y,M,Ms,c)
Constraints=y(1)==1;

for i=1:length(M)
    for j=1:i-1
        m1=M(i,i);m2=M(i,j);m3=M(j,j);
        Constraints=[Constraints,[m1 m2;m2 m3]>=0];
    end
end

for i=1:length(Ms)
    Me=Ms{i};
    for j=1:length(Me)
        for k=1:j-1
            m1=Me(i,i);m2=Me(i,j);m3=Me(j,j);
            Constraints=[Constraints,[m1 m2;m2 m3]>=0];
        end
    end
end
Obj=c'*y;
op=sdpsettings;op.verbose=0;op.solver='mosek';
res=optimize(Constraints,Obj,op);
if res.problem==0
    y=value(y);
else
    y=[];
end
end