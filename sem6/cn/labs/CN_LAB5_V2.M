%1
m = 5;
n = 2*m;
time = [0 3 5 8 13];
distance = [0 225 383 623 993];
speed = [75 77 80 74 72];

function table=div_dif_double(nodes,values,der_values)
n=2*length(nodes);
table=NaN(n);
double_nodes=repelem(nodes,2);
table(:,1)=repelem(values,2);
table(1:2:end-1,2)=der_values;
table(2:2:end-2,2)=diff(values)'./diff(nodes)';
for j=3:n
    for i=1:n-j+1
        table(i,j)=(table(i+1,j-1)-table(i,j-1))/(double_nodes(i+j-1)-double_nodes(i));
    end
end
end

function [Hx, der_Hx]=Hermite_interp(nodes,values,der_values,x)
    table=div_dif_double(nodes,values,der_values);
    coefs=table(1,:);
    double_nodes=repelem(nodes,2);
    Hx = x; der_Hx=x;
    for i=1:length(x)
        Hx(i)=coefs(1);
        p=1;
        der_Hx(i)=0;
        der_p=0;
        for k=2:length(coefs)
            der_p=der_p*(x(i)-double_nodes(k-1))+p;
            p=p*(x(i)-double_nodes(k-1));
            Hx(i)=Hx(i)+coefs(k)*p;
            der_Hx(i)=der_Hx(i)+coefs(k)*der_p;
        end
    end
endfunction
[Hx, der_Hx]=Hermite_interp(time,distance,speed,[10]);
printf("speed: %f, distance: %f", der_Hx, Hx)


%2
x=[1 2];
f=[0 0.6931];
fd=[1 0.5];
[Hx, der_Hx] = Hermite_interp(x,f,fd,3/2);
error = abs(log10(1.5)-Hx);
printf("\nvalue: %f, error: %f", Hx,error)


%3
clear
xplot1=-5:0.01:5;
fplot1=sin(2*xplot1);
figure
plot(xplot1,fplot1);
hold on
grid on
nodes1 = linspace(-5,5,15);
fnodes1 = sin(2*nodes1);
fdnodes1 = 2*cos(2*nodes1);
Hx=zeros(size(xplot1));  
for i=1:length(xplot1)
    [Hx(i), der_Hx(i)] = Hermite_interp(nodes1,fnodes1,fdnodes1,xplot1(i));
end
plot(xplot1,Hx);
plot(nodes1,fnodes1,'o');
legend('function','interpolation','nodes')


