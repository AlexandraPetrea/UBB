function[x] = NB(N,p)
for i= 1:1000
  SUM=0;
  for j=1:N
     geoSum=0;
     x=0;
     while(x != 1)
         geoSum = geoSum+1;
         n = rand();
         if n > p
              x = 0
          else 
               x = 1
          endif
       endwhile
   SUM=SUM+geoSum
 endfor
 disp(SUM)
endfor
end
 
