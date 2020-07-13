% Lab4, problem 2a
xvalues = [1 1.5 2 3 4];
yvalues = [0 0,17609 0.30103 0.47712 0.60206];
x = 2.5;
lagrange_int(x, xvalues, yvalues)

%2b
xvalues2 = [1 2 3 4 5];
yvalues2 = [22 23 25 30 28];
plot(xvalues2, yvalues2, 'o')
hold on
x = linspace(1,5);
plot(X, lagrange_int(X, xvalues2, yvalues2))
hold off