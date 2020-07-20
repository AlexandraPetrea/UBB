function[x] = bino(n,p)
for i=1:1000
  sum=0;
  for j=1:n
    if rand() > p
      sum = sum + 1;
    endif
   disp(sum)
endfor
end
