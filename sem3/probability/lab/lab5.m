X = [ 7,7,4,5,9,9; 
4,12,8,1,8,7;
3,13,2,1,17,7;
12,5,6,2,1,13;
14,10,2,4,9,11; 
3,5,12,6,10,7]

X1 = mean(X)
alpha = 0.05
z = norminv(1 - alpha/2)
sigma = 5
n = 10
rez = ( X1 - Z * sigma / sqrt(n), X1 + Z * sigma/sqrt(n))