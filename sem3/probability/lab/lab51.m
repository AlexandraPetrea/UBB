X=[ 7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7]

X1 = mean(X)

alpha = 0.010;

s = sqrt(var(X));

n = sqrt(length(X));

sigma=5;

z = norminv(1-alpha/2);

t = tinv(alpha/2, n-1);

sigma=sqrt(var(X));

z=norminv(1-alpha/2);

disp("A:");
disp(X1-z*(sigma/sqrt(size(X)(1))))
disp(X1+z*(sigma/sqrt(size(X)(1))))                                  


disp('B:')
disp(X1 - t * s / n)
disp(X1 + t * s/n)


disp('C:')

aux = chi2inv(1-alpha/2, n-1);
aux2 = chi2inv(alpha/2,n-1);
rez = ((n-1) * power(s,2))/aux;
disp(rez)
rez2 = ((n-1) * power(s,2))/aux2;
disp(rez2)
