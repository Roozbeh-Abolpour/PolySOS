function y=sos_sdp(y,M,Ms,c)
Constraints=[y(1)==1,M>=0];
for i=1:length(Ms)
    Constraints=[Constraints,Ms{i}>=0];
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