#https://www.hackerrank.com/challenges/standard-deviation-puzzles-1/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

orig_set=[1, 2, 3]
n=3

def stdDev(arr):
    n=len(arr)
    mean=float(sum(arr)/n)
    sods=0.0
    for i in range(n):
        sods=sods + (float(arr[i])-mean)**2
    sd=round((sods/n)**(1/2),6)
    return(sd)

sd_set = stdDev(orig_set)
x_min=2
x_max=10

def solveN(xmin, xmax,sd, arr):
  N=(xmin+xmax)*0.5
  arr.append(N)
  n=len(arr)
  mean=float(sum(arr)/(n))
  sd2=stdDev(arr)
  #return sd2
  
  while (abs(sd2-sd_set)!=0):
    if (sd2>sd_set):
      xmax=N
      N=(xmin+xmax)*0.5
    else:
      xmin=N
      N=(xmin+xmax)*0.5
    arr[3]=N
    #return arr
    #return sum(arr)
    mean=float(sum(arr)/(n))
    #return mean
    sd2=stdDev(arr)
    #return sd2
    
  return N

print(round(solveN(x_min, x_max, sd_set, orig_set),2))
