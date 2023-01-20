#https://www.hackerrank.com/challenges/poisson-distribution-5/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

lambda_=1.2
#print(lambda_)

def poisson(k,mean):
    return (math.pow(mean,k)*math.pow(math.e,-mean))/math.factorial(k)

#Q1
print(format(poisson(2,lambda_),".3f"))

#Q2
print(round(poisson(0,lambda_)+poisson(1,lambda_)+poisson(2,lambda_),3))

#q3
n=10
print(round(poisson(5,n*lambda_),3))

#q4
n=40
value=poisson(0,n*lambda_)+poisson(1,n*lambda_)+poisson(2,n*lambda_)
#print(value)
print(round(1-value,3))
