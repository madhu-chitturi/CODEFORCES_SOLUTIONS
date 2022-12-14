'''                                                              A. Lucky?

A ticket is a string consisting of six digits. A ticket is considered lucky if the sum of the first three digits is equal to the sum of the last three digits. Given a ticket, output if it is lucky or not. Note that a ticket can have leading zeroes.

Input
The first line of the input contains an integer t (1≤t≤103) — the number of testcases.

The description of each test consists of one line containing one string consisting of six digits.

Output
Output t lines, each of which contains the answer to the corresponding test case. Output "YES" if the given ticket is lucky, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

Example
inputCopy
5
213132
973894
045207
000000
055776
outputCopy
YES
NO
YES
YES
NO

SOLUTION <===================PYTHON===================>'''

t=int(input())
for k in range(t):
     a=input()
     b=list(map(int,str(a)))
     sum1=0
     sum2=0
     n=len(b)
     for i in range(0,3):
         sum1+=b[i]
     for j in range(n-3,n):
         sum2+=b[j]
     if(sum1==sum2):
         print("YES")
     else:
         print("NO")
