close all
clear
clc
d=2;
pc=[3 0 2;1 2 1;0 1 1];
p1=[0 0 1;2 0 -1;0 2 -1];
p2=[0 0 1;1 0 1;0 3 -1;1 1 1];
p3=[0 2 -1;2 0 -1;0 0 1];
ps={p1,p2,p3};
yalmip('clear')

[y,M,Ms,c]=sos_relaxation(pc,ps,d);
y_sdp=sos_sdp(y,M,Ms,c);

y_socp=sos_socp(y,M,Ms,c);

p0=0.8;
y_chordal_sdp=sos_chordal_sdp(y,M,Ms,c,p0);

fprintf('=== RESULTS ===\n\n');

fprintf('SDP solution:\n');
disp(y_sdp)

fprintf('Objective (SDP): %f\n\n', c'*y_sdp);

fprintf('SOCP solution:\n');
disp(y_socp)

fprintf('Objective (SOCP): %f\n\n', c'*y_socp);

fprintf('Chordal SDP solution:\n');
disp(y_chordal_sdp)

fprintf('Objective (Chordal SDP): %f\n\n', c'*y_chordal_sdp);

fprintf('=== COMPARISON ===\n');
fprintf('||SDP - SOCP||_inf = %e\n', norm(y_sdp - y_socp, inf));
fprintf('||SDP - Chordal||_inf = %e\n', norm(y_sdp - y_chordal_sdp, inf));