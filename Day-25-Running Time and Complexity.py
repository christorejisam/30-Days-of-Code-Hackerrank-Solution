# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
n = int(input())
def  Prime(n):
    for i in range(2,int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for i in range(n):
    no = int(input())
    if (no >=2 and Prime(no)):
        print("Prime")
    else:
        print("Not prime")
