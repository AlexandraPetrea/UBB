%1 
A = [ 3 -1  0  0  0  0;
     -1  3 -1  0  0  0;
      0 -1  3 -1  0  0;
      0  0 -1  3 -1  0;
      0  0  0 -1  3 -1;
      0  0  0  0 -1  3 ];

b = [2; 1; 1; 1; 1; 2];

function ret = solve(A, b, er)
  [n, n] = size(A);
  x = rand(n, 1);
  new_x = rand(n, 1);
  cnt = 0;
  while(norm(x - new_x) > er)
    cnt = cnt + 1;
    x = new_x;
    new_x = zeros(n, 1);
    for i=1:n
      new_x(i) = 1 / A(i, i) * (b(i) - A(i,1:i-1) * x(1:i-1) - A(i,i+1:n) * x(i+1:n));
    end
  end
  cnt
  ret = x;
end

solve(A, b, 0.00001)

%2
A2 = [ 3 -1  0  0  0  0;
     -1  3 -1  0  0  0;
      0 -1  3 -1  0  0;
      0  0 -1  3 -1  0;
      0  0  0 -1  3 -1;
      0  0  0  0 -1  3 ];

b2 = [2; 1; 1; 1; 1; 2];

A1 = [ 3  1  1;
      -2  4  0;
      -1  2 -6 ];

b1 = [12; 2; -5]

function ret = solve2(A, b, er)
  [n, n] = size(A);
  x = rand(n, 1);
  new_x = rand(n, 1);
  M = diag(diag(A));
  N = M - A;
  T = M \ N;
  c = M \ b;
  cnt = 0;
  while(norm(x - new_x) > er * (1 - norm(T)) / norm(T))
    x = new_x;
    new_x = T * x + c;
    cnt = cnt + 1;
  end
  cnt
  ret = x;
end

solve(A2, b2, 0.00001)
solve(A1, b1, 0.00001)