import sys

dna = sys.stdin.readline().rstrip()

complementary = ""

for n in dna:
    if n == 'A':
        complementary = complementary + 'T'
    elif n == 'T':
        complementary = complementary + 'A'
    elif n == 'G':
        complementary = complementary + 'C'
    elif n == 'C':
        complementary = complementary + 'G'

print(complementary[::-1])
