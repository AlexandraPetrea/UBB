% 0) i: number of files stored
x = [7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7];
sigma = 5; % known variance

% 1) test data: average number of stored files

% 2) null hypothesis H0
t0a = 9; %

% 3) observed data
t1a = mean(x); % lower than H0 since we do a left test

fprintf("Mean value: tt=%4.4f\n", t1a);
% 4) alternate hypothesis H1
% average number of stored files is lower than 9

% 5) test statistic
n = length(x);
tt = (t1a - t0a) / (sigma / sqrt(n));
fprintf("Test statistic: tt=%4.4f\n", tt);

% 6) significance level
alpha = 0.05;
rr = norminv(alpha);
fprintf("Rejection region: (-inf, %4.4f)\n", rr);

% 7) p-value
pa = normcdf(tt);
fprintf("Significance level: %.2f, P-Value: p=%4.4f\n", alpha, p);

% 8) conclusion
if (pa < alpha)
  fprintf("Reject H0, accept H1. average number of stored files is lower than 9\n");
else
  fprintf("Accept H0, reject H1. average number of stored files is NOT lower than 9\n");
end
fprintf("\nPUNCTUL B\n");

% 2) null hypothesis H0
t0b = std(x); % we calculate mean(x)

% 3) observed data
t1b = mean(x); % higher than H0 since we do a right test

% 4) alternate hypothesis H1
% average average number of files stored is higher than 5.5

% 5) test statistic
ttb = (t1b - t0b) / (sigma / sqrt(n));
fprintf("Test statistic: tt=%4.4f\n", ttb);

% 6) significance level
alphab = 0.05;
rrb = tinv(1 - alphab, n - 1);
fprintf("Rejection region: (%4.4f, inf)\n", rrb);

% 7) p-value
pb = 1 - tcdf(tt, n - 1);
fprintf("Significance level: %.2f, P-Value: p=%4.4f\n", alphab, pb);

% 8) conclusion
if (pb < alpha)
  fprintf("Reject H0, accept H1. average average number of files stored is higher than 5.5\n");
else
  fprintf("Accept H0, reject H1. average average number of files stored is NOT higher than 5.5\n");
end