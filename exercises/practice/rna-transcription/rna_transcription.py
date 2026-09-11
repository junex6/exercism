def to_rna(dna_strand):
    trans_table = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(trans_table)
