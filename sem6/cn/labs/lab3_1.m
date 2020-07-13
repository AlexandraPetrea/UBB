
x= [1930 1940 1950 1960 1970 1980];
y = [123203 131669 150697 179323 203212 226505];

function L = polinomial_interpolation(x, y, X)

    m = length(x);
    A = ones(1, m);
    for k = 1:length(X)
        s1 = 0;
        s2 = 0;
        
        for i = 1:m
            A(i) = 1 ./ prod(x(i) - x([1:i-1, i+1:m]));
        end
        
        for i = 1:m
            s2 = s2 + (A(i) / (X(k) - x(i) + eps));
            s1 = s1 + ((A(i) * y(i)) / (X(k) - x(i) + eps));
        end
        
        L(k) = s1 / s2;
    end
endfunction

polinomial_interpolation(x, y, 1955)
polinomial_interpolation(x, y, 1995)
