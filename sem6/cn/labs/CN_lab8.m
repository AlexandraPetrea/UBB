%1
%a
a=0;
b=1;
f=@(x) 2./(1+x.^2);
trp = ((b-a)/2)*(f(a)+f(b));
fprintf('Ex 1 a) Approx using trapezium = %2.5f\n',trp);


%b
xplot = 0:0.01:1;
fplot = f(xplot);
figure
plot(xplot,fplot)
hold on
grid on
x_trap = [0 0 1 1];
y_trap = [0 f(0) f(1) 0];
plot(x_trap,y_trap)

%c
simp = ((b-a)/6)*(f(a) + 4*f((a+b)/2)+f(b));
fprintf('Ex 1 c) Approx using Simpson = %2.5f\n',simp);

%2
clear
fprintf('\n')
a=1.4;
b=2;
c=1;
d=1.5;
f=@(x,y) log(x+2*y);
trap = (((b-a)*(d-c))/16) * ( f(a,c) + f(a,d) + f(b,c) + f(b,d) + 2*f((a+b)/2,c)+ 2*f((a+b)/2,d)+ 2*f(a,(c+d)/2) + 2*f(b,(c+d)/2) + 4* f((a+b)/2,(c+d)/2)); 
fprintf('Ex 2 Approximation for integral = %2.5f, correct value is %2.5f\n',trap, 0.4295545);

%3
clear
fprintf('\n')
p=75;
r=110;
a=0;
b=2*pi;
f=@(x) (1-((p/r)^2).*sin(x)).^(1/2);

n=10;
h=(b-a)/n;
xk = a + (0:n)*h;
reptrap = ((b-a)/(2*n)) * (f(a)+ f(b) + 2*sum(f(xk(2:n))));
approx = ((60*r)/(r^2-p^2))*reptrap;
fprintf('Ex 3 Approx with n=10 is %2.5f\n',approx);
n=20;
h=(b-a)/n;
xk = a + (0:n)*h;
reptrap = ((b-a)/(2*n)) * (f(a)+ f(b) + 2*sum(f(xk(2:n))));
approx2 = ((60*r)/(r^2-p^2))*reptrap;
fprintf('Ex 3 Approx with n=20 is %2.5f\n',approx2);

%4
clear
fprintf('\n')
a=1;
b=2;
f=@(x) x.*log(x);
n=10;
h=(b-a)/n;
xk = a + (0:n)*h;
reptrap = ((b-a)/(2*n)) * (f(a)+ f(b) + 2*sum(f(xk(2:n))));
fprintf('Ex 4 Approx for n=%d is %2.5f, correct value is %2.5f\n',n,reptrap, 0.6362943688583);

%5
clear
fprintf('\n')
a=0;
b=pi;
f=@(x) 1./(4+sin(20*x));

n=10;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
fprintf('Ex 5 Approx with n=10 is %2.5f\n',approx);

n=30;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
fprintf('Ex 5 Approx with n=30 is %2.5f, correct value is: %2.5f\n',approx, 0.81115);

%6
clear
fprintf('\n');
a=0;
b=0.5;
f=@(t) exp(1).^(-t.^2);

n=4;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
res= (2/sqrt(pi))*approx;
fprintf('Ex 6 Approx with n=%d is %2.9f, actual result = %2.9f\n',n,res,0.520499876);

n=10;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
res= (2/sqrt(pi))*approx;
fprintf('Ex 6 Approx with n=%d is %2.9f, correct value is: %2.9f\n',n,res,0.520499876);

