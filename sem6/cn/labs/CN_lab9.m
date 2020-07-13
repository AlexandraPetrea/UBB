%1
%a
a=1; b=1.5;
x1=[1:1.5:100];
f=@(x) exp(1).^(-x.^2);
rectangle = (b-a)*f((a+b)/2);
fprintf('The exact value = %2.5f\n', 0.1094);
fprintf('Ex 1 a) Rectangle approx = %2.5f\n',rectangle);
plot(x1,f(x1))
hold on

%c
n=150;
x1=a+ (b-a)/(2*n);
xi=x1+(1:n-1)*(b-a)/n;
reprectangle = ((b-a)/n)*sum(f(xi));
fprintf('Ex 1 b) Repeated rectangle approx with n=150 is %2.5f\n',reprectangle);
plot (reprectangle)
hold off;
n=500;
x1=a+ (b-a)/(2*n);
xi=x1+(1:n-1)*(b-a)/n;
reprectangle = ((b-a)/n)*sum(f(xi));
fprintf('Ex 1 b) Repeated rectangle approx with n=500 is %2.5f\n',reprectangle);




%2
clear
fprintf('\n');
a=0; b=1;
f=@(x) 2./(1+x.^2);
h=b-a;
qt0 = (h/2)*(f(a)+f(b));
qt1 = (h/4)*(f(a)+2*f(a+h/2)+f(b));
q = [qt0 qt1];
i = 2;
eps =10^(-5);
while abs(q(end)-q(end-1))>eps
    j= 1:2^i;
    elems = a + h*(2*j-1)./(2^(i+1));
    qtemp = 0.5*q(i) + (h/(2^(i+1)))*sum(f(elems));
    q=[q qtemp];
    i=i+1;
end
fprintf('Ex 2 Romberg’s algorithm approx = %2.5f for k=%d\n',q(end),i);

qs0 = (h/6)* (f(a)+4*f(a+h/2)+f(b));
qs1 = (1/3)*(4*q(2)-q(1));
i=3;
qsimp=[qs0 qs1];
while abs(qsimp(end)-qsimp(end-1))>eps
    qtemp = (1/3)*(4*q(i+1)-q(i));
    qsimp=[qsimp qtemp];
    i=i+1;
end
fprintf('Ex 2 Simpson approx = %2.5f for k=%d\n',qsimp(end),length(qsimp));
%3
function S = Simpson( a,b,f )
    S = ((b-a)/6)*(f(a) + 4*f((a+b)/2)+f(b));
end

function I = adquad( a,b,f,er )
    I1=Simpson(a,b,f);
    I2=Simpson(a,(a+b)/2,f)+Simpson((a+b)/2,b,f); 
    if abs(I1-I2)<15*er
        I=I2;
        return
    else
        I=adquad(a,(a+b)/2,f,er/2)+adquad((a+b)/2,b,f,er/2);
    end
end


clear
fprintf('\n');
xplot = 1:0.01:3;
f=@(x) (100./x.^2).*sin(10./x); 
fplot=f(xplot);
figure
plot(xplot,fplot);
hold on
fprintf('The exact value = %2.5f\n', -1.4260247818);


a=1;b=3;
AdQuadRes = adquad(a,b,f,10^(-4));
fprintf('Ex 3 Adaptive quadrature approx = %2.5f\n',AdQuadRes);

n=50;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
fprintf('Ex 3 Repeated Simpson for n=%d, approx = %2.5f\n',n,approx);

n=100;
h=(b-a)/n;
xk = a + (0:n)*h;
approx = ((b-a)/(6*n))* (f(a)+f(b)+2*sum(f(xk(2:n)))+4*sum(f((xk(1:n)+xk(2:n+1))/2)));
fprintf('Ex 3 Repeated Simpson for n=%d, approx = %2.5f\n',n,approx);

