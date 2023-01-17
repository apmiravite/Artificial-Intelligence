# Enter your code here. Read input from STDIN. Print output to STDOUT

from fractions import Fraction
d1=[i+1 for i in range(6)]
d2=[i+1 for i in range(6)]

counter=int(0)
throws=int(0)
for i in range(6):
    for j in range(6):
        sum_toss=0
        sum_toss=d1[i-1]+d2[j-1]
        #print(sum_toss)
        throws=throws+1
        if(sum_toss<=9):
            counter=counter+1
    
#print(counter)
#print(throws)

def gcd(n,d):
    residual =int(d)
    while (residual!=0):
        residual = d%n
        #print(residual)
        d=n
        n=residual
    return d
        
gcd = gcd(counter, throws)
#print(gcd)

print(Fraction(int(counter/gcd), int(throws/gcd)))
