X = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0]
Y = [ 17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2]

len1 = length(X)
len2 = length(Y)
s1 = var(X)
s2 = var(Y)

s = sqrt(((len1-1)*s1*s1 + (len2-1)*s2*s2)/(len1+len2-2))
disp(s)

v = power((s1*s1/len1 + s2*s2/len2),2)/ (power(s1,4)/len1*len1*(len1-1) + 
power(s2,4)/len2*len2*(len2-1))
disp(v)

alpha = input('Give the alpha=')
x_min = (s1 /s2 ) * ( 1 / finv(alpha/2,len1-1,len2-1));
x_max = (s1/s2) * finv(alpha/2, len2-1, len1-1);
disp(x_min)
disp(x_max)