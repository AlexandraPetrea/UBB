function[x] = geo(p)
   for i=1:1000
     sum=0;
     x=0;
     while(x != 1)
         sum = sum+1;
         n = rand();
         if n > p
              x = 0
          else 
               x = 1
          endif
       endwhile
      disp(sum)
 endfor
