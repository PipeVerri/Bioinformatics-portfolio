from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
Entrez.email = "pipe.verri@gmail.com"

ids = input().split(" ")
stream_0 = Entrez.efetch(db="nucleotide", id=ids[0], rettype="gb", retmode="text")
seq_0 = SeqIO.read(stream_0, "genbank").seq
stream_1 = Entrez.efetch(db="nucleotide", id=ids[1], rettype="gb", retmode="text")
seq_1 = SeqIO.read(stream_1, "genbank").seq

aligner = PairwiseAligner()
aligner.mode = "global"
aligner.substitution_matrix = substitution_matrices.load("NUC.4.4")
aligner.open_gap_score = -10
aligner.extend_gap_score = -1
alignment = aligner.align(seq_0, seq_1)
print(int(alignment[0].score))