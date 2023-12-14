idle = [1] * 480
n = int(input("input n:"))
print(n)
for i in range(0, n):
    x = int(input("in_time :"))
    y = int(input("out_time:"))
    for j in range(x, y+1):
        idle[j] = 0
print(sum(idle[0:480]))
