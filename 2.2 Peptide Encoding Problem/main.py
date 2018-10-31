import sys

table = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': ' ',
    'UAC': 'Y',
    'UAG': ' ',
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': ' ',
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F'
}


def reverse(dna):
    complementary = ""

    for n in dna:
        if n == 'A':
            complementary = complementary + 'U'
        elif n == 'U':
            complementary = complementary + 'A'
        elif n == 'G':
            complementary = complementary + 'C'
        elif n == 'C':
            complementary = complementary + 'G'
    return complementary[::-1]


def build_peptide(part):
    peptide = ""
    for i in range(0, len(part), 3):
        peptide += table[part[i:i+3]]
    return peptide


def main():
    rna = sys.stdin.readline().rstrip()
    peptide = sys.stdin.readline().rstrip()

    compl = rna.replace('T', 'U')

    for i in range(len(compl) - len(peptide)*3+1):
        part = compl[i:i+len(peptide)*3]
        if peptide == build_peptide(part) or peptide == build_peptide(reverse(part)):
            print(rna[i:i+len(peptide)*3])


if __name__ == "__main__":
    main()
