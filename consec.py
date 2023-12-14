n = 8
start = 1
end = int((n+1)/2)
sum = 0
chk = 1
while(start < end):
    for i in range(start, end+1):
        sum = sum +i
        if sum == n :
            for j in range(start, i+1):
                chk = 0
                print(j, end=" ")
            print()
        if sum > n: break;
    start = start + 1
    sum = 0

if chk == 1: print("NO")