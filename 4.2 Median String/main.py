import itertools
import sys


def hamming(a, b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter


def d(pattern, text):
    k = len(pattern)
    dist = list(hamming(pattern, text[i:i + k]) for i in range(len(text) - k + 1))
    return min(dist)


def ddna(pattern, dna):
    sum = 0
    for dnai in dna:
        sum += d(pattern, dnai)
    return sum


def median_string(dna, k):
    distance = sys.maxsize
    median = ""
    alphabet = "AGCT"
    all_kmers = map(''.join, itertools.product(alphabet, repeat=k))
    for kmer in all_kmers:
        if distance > ddna(kmer, dna):
            distance = ddna(kmer, dna)
            median = kmer

    return median


def main():
    k = int(sys.stdin.readline().rstrip())
    dna = []

    s = sys.stdin.readline()
    while s != "\n" and s != "":
        dna.append(s.rstrip())
        s = sys.stdin.readline()
    print(median_string(dna, k))


if __name__ == '__main__':
    main()
