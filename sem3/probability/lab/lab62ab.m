x = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0];
y = [17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2];

vx = var(x); % unknown variance of x, sampled from data
vy = var(y); % unknown variance of y, sampled from data
fprintf("vx =%.2f\n", vx);

fprintf("vy = %.2f\n", vy);
% 1) test data: two variances of gas mileage

% 2) null hypothesis H0
t0 = 1; % assume var(premium) = var(regular)

% 3) observed data
t1 = vx / vy; % any relation to t0 since we do an equality test

% 4) alternate hypothesis H1
% variance of premium gasoline is DIFFERENT from variance of regular gasoline

% 5) test statistic
nx = length(x);
ny = length(y);
tt = t1;
fprintf("Test statistic: tt=%4.4f\n", tt);

% 6) significance level
alpha = 0.05;
rrl = finv(alpha / 2, nx - 1, ny - 1);
rrr = finv(1 - alpha / 2, nx - 1, ny - 1);
fprintf("Rejection region: (-inf, %4.4f) U (%4.4f, inf) \n", rrl, rrr);

% 7) p-value
pl = fcdf(tt, nx - 1, ny - 1);
pr = 1 - fcdf(tt, nx - 1, ny - 1);
p = 2 * min(pl, pr);
fprintf("Significance level: %.2f, P-Value: p=%4.4f\n", alpha, p);

% 8) conclusion
if (p < alpha)
  fprintf("Reject H0, accept H1. variance of premium gasoline is DIFFERENT from variance of regular gasoline\n");
else
  fprintf("Accept H0, reject H1. variance of premium gasoline is EQUAL to variance of regular gasoline\n");
end

fprintf("\nPUNCTUL B\n")

nx = length(x);
ny = length(y);
ux = mean(x);
uy = mean(y);

% 1) test data: two average gas mileages

% 2) null hypothesis H0
t0 = 0; % assume mean(premium) = mean(regular)

% 3) observed data
t1 = ux - uy; % observe mean(premium) > mean(regular)
fprintf("T1 %4.4f\n", t1);
% 4) alternate hypothesis H1
% premium mileage is higher than regular mileage

% 5) test statistic
sp = sqrt(((nx - 1) * vx + (ny - 1) * vy) / (nx + ny - 2));
fprintf("Sp: %.2f\n", sp);

tt = t1 / (sp * sqrt(1 / nx + 1 / ny));
fprintf("Test statistic: tt=%4.4f\n", tt);

% 6) significance level
alpha = 0.05;
rr = tinv(1 - alpha, nx + ny - 2);
fprintf("Rejection region: (%4.4f, inf)\n", rr);

% 7) p-value
p1 = 1 - tcdf(tt, nx + ny - 2);
fprintf("Significance level: %2.2f, P-Value: p=%4.4f\n", alpha, p1);

% 8) conclusion
if (p1 < alpha)
  fprintf("Reject H0, accept H1. premium mileage is higher than regular mileage\n");
else
  fprintf("Accept H0, reject H1. premium mileage is NOT higher than regular mileage\n");
end