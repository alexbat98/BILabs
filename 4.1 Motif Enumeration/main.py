import sys
import itertools


def isKDmer(kMer, candidate, d):
    mismatchCount = 0
    for i in range(len(kMer)):
        if kMer[i] != candidate[i]:
            mismatchCount += 1
        if mismatchCount > d:
            return False
    return True


def getAllKDMers(kMer, d):
    alphabet = "AGCT"
    kdMers = []
    allKmers = map(''.join, itertools.product(alphabet, repeat=len(kMer)))

    for candidate in allKmers:
        if isKDmer(kMer, candidate, d):
            kdMers.append(candidate)

    return kdMers


def main():
    kd = sys.stdin.readline().rstrip()
    kd = kd.split(" ")
    k = int(kd[0])
    d = int(kd[1])
    dna = []

    s = sys.stdin.readline()
    while s != "\n" and s != "":
        dna.append(s.rstrip())
        s = sys.stdin.readline()

    patterns = []

    for dna_par in dna:
        kmers = list(dna_par[i:i+k] for i in range(len(dna_par) - k + 1))
        for kmer in kmers:
            kdmers = getAllKDMers(kmer, d)
            for kdmer in kdmers:
                count = 0
                for dna_str in dna:
                    kmers_2 = list(dna_str[i:i + k] for i in range(len(dna_str) - k + 1))
                    for km in kmers_2:
                        if isKDmer(kdmer, km, d):
                            count += 1
                            break
                if count == len(dna):
                    patterns.append(kdmer)

    print(" ".join(set(patterns)))


if __name__ == '__main__':
    main()
