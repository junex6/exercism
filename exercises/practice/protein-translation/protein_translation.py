CODON_TO_AMINO_ACID = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine",       "UUG": "Leucine",
    "UCU": "Serine",        "UCC": "Serine", 
    "UCA": "Serine",        "UCG": "Serine",
    "UAU": "Tyrosine",      "UAC": "Tyrosine",
    "UGU": "Cysteine",      "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

STOP_CODONS = {"UAA", "UAG", "UGA"}

def proteins(strand):
    amino_acid = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3] 
        if codon in STOP_CODONS:
            break
        else:
            amino_acid.append(CODON_TO_AMINO_ACID[codon])
    return amino_acid
