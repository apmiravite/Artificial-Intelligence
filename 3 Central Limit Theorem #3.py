#https://www.hackerrank.com/challenges/the-central-limit-theorem-3/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

n=100
mean=500
sigma=80
sample_sigma=80/math.pow(n,0.5)

test=statistics.NormalDist(mean, sample_sigma)


lower=490
upper=510

upper_p=(test.cdf(upper))
lower_p=(test.cdf(lower))
print(round(upper_p-lower_p,4))
