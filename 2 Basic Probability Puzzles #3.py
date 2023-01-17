#https://www.hackerrank.com/challenges/basic-probability-puzzles-3/problem

#Urn X contains 4 red balls and 3 black balls
#Urn Y contains 5 red balls and 4 black balls
#Urn Z contains 4 red balls and 4 black balls
#select 1 ball from each urn, what is the probability that the 3 balls drawn consist of 2 red balls and 1 black ball?

# Enter your code here. Read input from STDIN. Print output to STDOUT

from fractions import Fraction

X=["R", "R", "R", "R", "B", "B", "B"]
Y=["R", "R", "R", "R", "R", "B", "B", "B", "B"]
Z=["R", "R", "R", "R", "B", "B", "B", "B"]

counter=0
total=504
for x1 in X:
    for y1 in Y:
        for z1 in Z:
            if (x1=="R" and y1=="R" and z1=="B") or (x1=="R" and y1=="B" and z1=="R") or (x1=="B" and y1=="R" and z1=="R"):
                counter=counter+1

def gcd(n,d):
    residual =int(d)
    while (residual!=0):
        residual = d%n
        #print(residual)
        d=n
        n=residual
    return d
        
gcd = gcd(counter, total)

print(Fraction(int(counter/gcd), int(total/gcd)))
