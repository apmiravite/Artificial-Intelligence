#https://www.hackerrank.com/challenges/poisson-distribution-3/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

lambda_=3
value=0
#print(lambda_)
#print(value)

def poisson(k,mean):
    return (math.pow(mean,k)*math.pow(math.e,-mean))/math.factorial(k)

print(format(poisson(value,lambda_),".3f"))

value2=round(poisson(0,lambda_)*poisson(0,lambda_)+poisson(0,lambda_)*poisson(1,lambda_)+poisson(1,lambda_)*poisson(0,lambda_),3)
print(1-value2)
