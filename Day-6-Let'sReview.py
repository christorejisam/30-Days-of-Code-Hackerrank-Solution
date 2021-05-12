# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for i in range(0, N):
 
    string = input()
    
    for i in range(0, len(string)):
        if i % 2 == 0:
            print(string[i], end='')

    print(" ", end='') 
    
    for i in range(0, len(string)):
        if i % 2 !=0:
            print(string[i], end='')

    print()