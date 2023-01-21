#https://www.hackerrank.com/challenges/stat-warmup/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

n=int(input())
arr = list(map(int, input().split()))
print(format(statistics.mean(arr),".1f"))
print(format(statistics.median(arr),".1f"))
print(statistics.mode(sorted(arr)))

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean=float(sum(arr)/n)
    sods=0.0
    for i in range(n):
        sods=sods + (float(arr[i])-mean)**2
    sd=round((sods/n)**(1/2),1)
    return sd
print(stdDev(arr))

print(format(statistics.mean(arr)-stdDev(arr)*1.96*math.pow(n,-0.5),".1f"),format(statistics.mean(arr)+stdDev(arr)*1.96*math.pow(n,-0.5),".1f") )
