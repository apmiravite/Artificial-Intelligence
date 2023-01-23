# https://www.hackerrank.com/challenges/from-paragraphs-to-sentences/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
paragraph=str(input())

for i in re.split("(?<=[.!?\"]) +", paragraph):
    print(i)
