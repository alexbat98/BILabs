import sys

mass_table = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

peptide = sys.stdin.readline().rstrip()

out_masses = [0]

m = 0
for s in peptide:
    out_masses.append(mass_table[s])
    m += mass_table[s]
out_masses.append(m)

cycle_peptide = peptide + peptide

for i in range(2, len(peptide)):
    for j in range(0, len(peptide)):
        subpeptide = cycle_peptide[j:j+i]
        mass = 0
        for s in subpeptide:
            mass += mass_table[s]
        out_masses.append(mass)

print(" ".join(str(x) for x in sorted(out_masses)))
