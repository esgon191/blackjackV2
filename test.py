a = [1, 2, 3, 4, 5, 6, 0]
ind = int(input())

for i in range(len(a)-1, ind, -1):
    a[i] = a[i-1]

print(a)
