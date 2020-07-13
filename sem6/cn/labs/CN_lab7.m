%1
xi=[1 2 3 4 5 6 7];
fi=[13 15 20 14 15 13 10];
m=length(xi)-1;
sumxi=sum(xi);
sumfi=sum(fi);
sumxifi=sum(xi.*fi);
sumxi2=sum(xi.^2);

a=((m+1)*sumxifi-sumxi*sumfi)/((m+1)*sumxi2-(sumxi)^2);
b=(sumxi2*sumfi-sumxifi*sumxi)/((m+1)*sumxi2-(sumxi)^2);

%polyfit(xi,fi,1)
pol=[a b];
rez = polyval(pol,8);
fprintf("f(8.00)=%2.4f\n",rez);
xplot = 1:0.01:8;
pplot = polyval(pol,xplot);
figure
plot(xi,fi,'x');
hold on;
grid on;
plot(xplot,pplot);
eab=sum((fi-(a*xi+b)).^2);
fprintf("E(a,b)=%2.4f\n",eab);
legend('Time/Temperature','Approximation');


%2
clear
x=[0 10 20 30 40 60 80 100];
f=[0.0061 0.0123 0.0234 0.0424 0.0738 0.1992 0.4736 1.0133];

p1 = polyfit(x,f,1);
p2 = polyfit(x,f,2);

rez1 = polyval(p1,45);
rez2 = polyval(p2,45);

fprintf("1st degree polynomial, error = %2.4f\n",0.095848-rez1);
fprintf("2nd degree polynomial, error = %2.4f\n",0.095848-rez2);

figure
plot(x,f,'x');
hold on;
grid on;
xplot=0:0.01:100;
plot(xplot,polyval(p1,xplot));
plot(xplot,polyval(p2,xplot));
legend('Nodes','1st degree','2nd degree');

%3
axis([0, 3, 0, 5])
[x, y] = ginput(10);

P2 = polyfit(x, y, 2);

hold on;
plot(x, y, 'x');
x_ext = 0:0.1:3
plot(x_ext, polyval(P2, x_ext));

