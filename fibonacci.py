n1 = 0
n2 = 1
seq = 6
print(n1, n2, end=" ")
for i in range(0 , seq-2):
    nx = n1 + n2
    n1 = n2
    n2 = nx
    print(nx, end=" ")
print(nx)
