%input data
x = [1001.7 975.0 978.3 988.3 978.7 988.9 1000.3 979.2 968.9 983.5 999.2 985.6];
sigma = std(x); % unknown variance 

% 1) test data: average muzzle velocites

% 2) null hypothesis H0
t0 = 995; % we assume muzzle are faster than 995 m/s

% 3) observed data
t1 = mean(x); % lower than H0 since we do a right test

% 4) alternate hypothesis H1
% average muzzle speed are lower than we assumed

% 5) test statistic
n = length(x);
tt = (t1 - t0) / (sigma / sqrt(n));
fprintf("Test statistic: tt=%4.4f\n", tt);

% 6) significance level
alpha = 0.05;
rr = tinv(1-alpha, n - 1);
fprintf("Rejection region: (%4.4f,inf)\n", rr);

% 7) p-value
p = 1-tcdf(tt, n - 1);
fprintf("Significance level: %.2f, P-Value: p=%4.4f\n", alpha, p);

% 8) conclusion
if (p < alpha)
  fprintf("Reject H0, accept H1.\n"); % Average speed is lower than assumed.
else
  fprintf("Accept H0, reject H1.\n"); % Average speed NOT lower than assumed.
end
fprintf("Punctul b:");
alfa = 0.01;

s_squared = var(x);
n = 12;
chi_1_squared = chi2inv(1-alfa/2,n-1);
chi_2_squared = chi2inv(alfa/2,n-1);
capat_stanga = ((n-1)*s_squared)/chi_1_squared;
capat_dreapta = ((n-1)*s_squared)/chi_2_squared;
%conf. interval for the standard deviation
capat_stanga2 = sqrt(capat_stanga);
capat_dreapta2 = sqrt(capat_dreapta);
fprintf('[%f  %f]\n', capat_stanga2, capat_dreapta2);