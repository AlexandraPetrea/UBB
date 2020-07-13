%1 
f = @(x) cos(x) - x
fd = @(x) -sin(x) - 1

function ret = newton(f, fd, x0, maxIter, err)
  for n = 1:maxIter
    x1 = x0 - f(x0) / fd(x0);
    if abs(x1 - x0) < err
      break
    end
    x0 = x1;
  end
  ret = x0
end

x = newton(f, fd,  pi/4, 100, 0.0001);

%2
f2 = @(x) x ^ 3 - x ^ 2 - 1

function ret = secant(f2, x0, x1, maxIter, err)
  for n = 1:maxIter
    if abs(x1 - x0) < err
      break
    end
    x = x1 - (x1 - x0) / (f2(x1) - f2(x0)) * f2(x1);
    x0 = x1;
    x1 = x;
  end
  ret = x1
end

x = secant(f2, 1, 2, 100, 0.0001);

%3
f3 = @(x3) (x3 - 2) ^ 2 - log(x3)

function ret = bisect(f3, a, b, err)
  for n = 0:1000
    if abs(a - b) < err
      break
    end
    c = (a + b) ./ 2;
    if f3(a) * f3(c) <= 0
      b = c;
    else
      a = c;
    end
  end
  ret = a
end

bisect(f3, 1, 2, 0.0001);