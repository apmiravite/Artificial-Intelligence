#https://www.hackerrank.com/challenges/poisson-distribution-1/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT


import math

lambda_=2.5
value=5
#print(lambda_)
#print(value)

def poisson(k,mean):
    return (math.pow(mean,k)*math.pow(math.e,-mean))/math.factorial(k)

print(round(poisson(value,lambda_),3))
