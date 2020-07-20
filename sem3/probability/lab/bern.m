function[x] = bern(p)
for i=1:1000
    n=rand();
    if n > p
         x = 0
    else 
         x = 1
    endif
endfor
end
