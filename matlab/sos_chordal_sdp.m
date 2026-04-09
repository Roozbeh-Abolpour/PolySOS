function y=sos_chordal_sdp(y,M,Ms,c,p0)
Constraints=y(1)==1;
n=size(M,1);
[V,E]=genChordalGraph(n,p0);
C=maxCliques(V,E);
for i=1:length(C)
    Constraints=[Constraints,M(C{i},C{i})>=0];
end
for i=1:length(Ms)
    Me=Ms{i};
    n=size(Me,1);
    [V,E]=genChordalGraph(n,p0);
    C=maxCliques(V,E);    
    for j=1:length(C)
        Constraints=[Constraints,Me(C{j},C{j})>=0];
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