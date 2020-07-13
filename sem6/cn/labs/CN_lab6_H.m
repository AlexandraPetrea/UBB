%1

x = [ 0 pi/2 3 * pi / 2 2 * pi];
f = sin(x);
f_d = cos(x);


sin(pi/4);
spline(x, f, pi/4);
spline(x, [f_d(1) f f_d(4)], pi/4);

aux = linspace(0, 2 * pi, 1000);
hold on
plot(aux, sin(aux));
plot(aux, spline(x, f, aux));
plot(aux, spline(x, [f_d(1) f f_d(4)], aux));
hold off

