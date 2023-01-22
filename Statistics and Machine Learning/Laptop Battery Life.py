#https://www.hackerrank.com/challenges/battery/problem?isFullScreen=true

#!/bin/python3

timeCharged = float(input())

if (timeCharged<4):
    print(format(timeCharged*2,".2f"))
else:
    print(format(8,".2f"))
