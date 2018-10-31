import sys

m = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

n = int(sys.stdin.readline().rstrip())

N = {0: 1}
for i in range(57, n+1):
    N[i] = 0
    for j in range(len(m)):
        if (i - m[j]) in N:
            N[i] += N[i-m[j]]

print(N[n])
