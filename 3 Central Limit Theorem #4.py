#https://www.hackerrank.com/challenges/the-central-limit-theorem-4/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

n=100
mean=500
sigma=80
conf=0.95
zscore=1.96
#print(n, mean, sigma, conf, zscore)

lower=mean-zscore*sigma*math.pow(100,-0.5)
upper=mean+zscore*sigma*math.pow(100,-0.5)
print(round(lower,2))
print(round(upper,2))
