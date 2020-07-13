%Lab4, problem 3
xvalues = linspace(0,6,13);
yvalues = exp(sin(x));
plot(xvalues,yvalues,'o');

X = linspace(0,6,200);
hold on
fplot(@(z) exp(sin(z)), [0,6])
plot(X, lagrange_int(x,f,X))
hold off