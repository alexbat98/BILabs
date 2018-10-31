import sys


def main():
    pattern = sys.stdin.readline().rstrip()
    dna = sys.stdin.readline().rstrip()
    print(len([i for i in range(len(dna)) if dna[i:i + len(pattern)] == pattern]))


if __name__ == '__main__':
    main()
