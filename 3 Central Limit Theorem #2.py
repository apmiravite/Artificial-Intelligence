#https://www.hackerrank.com/challenges/the-central-limit-theorem-2/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

max_load = 250
n=100
mean=2.4
sigma=2

test=statistics.NormalDist(mean*n, sigma*math.pow(n,0.5))
print(round(test.cdf(max_load),4))
