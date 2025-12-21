import sys
data=sys.stdin.read().strip().split()
it=iter(data)
n=int(next(it))
A=[int(next(it)) for _ in range(n)]
print(A)