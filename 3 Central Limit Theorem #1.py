#https://www.hackerrank.com/challenges/the-central-limit-theorem-2/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

max_load = 9800
n=49
mean=205
sigma=15

test=statistics.NormalDist(mean*n, sigma*math.pow(n,0.5))
print(round(test.cdf(max_load),4))
