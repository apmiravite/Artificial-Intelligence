# https://www.hackerrank.com/challenges/forecasting-passenger-traffic/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
t=[]
x=[]
for i in range(n):
   t_y_n=input().split()
   t.append(t_y_n[0])
   x.append(int(t_y_n[-1]))
#print(t)
#print(x)

m=12
for i in range(m):
    pred=int(sum(x[-12:])/12)
    x.append(pred)
    print(pred)
