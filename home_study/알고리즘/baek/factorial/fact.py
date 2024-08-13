import sys
sys.stdin = open("input.txt", "r")

N = int(input())

def fact(N):
    if N == 0:
        return 1
    else:
        return N * fact(N-1)

result = fact(N)
print(result)