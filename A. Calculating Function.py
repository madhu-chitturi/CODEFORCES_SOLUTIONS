  '''                                                      A. Calculating Function

For a positive integer n let's define a function f:

f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn

Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 1015).

Output
Print f(n) in a single line.

Examples
inputCopy
4
outputCopy
2
inputCopy
5
outputCopy
-3

SOLUTION <==================PYTHON================>  '''

n=int(input())
sum=0
if(n%2==0):
    sum=n//2
else:
    sum=((n+1)//2)*(-1)
print(sum)
