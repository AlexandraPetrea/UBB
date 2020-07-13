%Lab4, problem 1
xvalues = [1 1.5 2 3 4];
yvalues = [0 0,17609 0.30103 0.47712 0.60206];
x = [2.5 3.25];

function y = lagrange_int(x, xvalues, yvalues)
n = size(xvalues, 2);
A = ones(1, n);
for i = 1:n
    for j=1:n
        if(i ~= j)
            A(i) = A(i) ./ (xvalues(i) - xvalues(j));
        end
    end
end

number = 0;
denom = 0;
for i = 1:n
    number = number + ((A(i) .* yvalues(i)) ./ (x-xvalues(i)));
    denom = denom + ( ( A(i)) ./ (x - xvalues(i)));

end
y = number ./ denom;
end

z = lagrange_int(x, xvalues, yvalues);
yy = [10:35]/10;
error=abs(log10(yy)-lagrange_int(yy, xvalues, yvalues));
E= max(error)