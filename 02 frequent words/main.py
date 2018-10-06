import sys

dna = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())

max_count = -1
max_mers = []
flagged = []

for j in range(len(dna) - k):
    if not dna[j:j+k] in flagged:
        cur_count = len([i for i in range(len(dna)) if dna[i:i+k] == dna[j:j+k]])
        if cur_count > max_count:
            max_mers = [dna[j:j+k]]
            max_count = cur_count
        elif cur_count == max_count and not dna[j:j+k] in max_mers:
            max_mers.append(dna[j:j+k])

out = " ".join(max_mers)
print(out)
