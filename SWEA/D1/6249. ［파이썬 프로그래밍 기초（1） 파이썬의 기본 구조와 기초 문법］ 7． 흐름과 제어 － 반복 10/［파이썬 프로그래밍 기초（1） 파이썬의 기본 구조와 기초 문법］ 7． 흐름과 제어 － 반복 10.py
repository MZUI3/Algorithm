n = input()
arr = [0]*10
for N in n:
    arr[int(N)] += 1
for i in range(10):
    print(i, end=" ")
print()
for i in range(10):
    print(arr[i], end=" ")