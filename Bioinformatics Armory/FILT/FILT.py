from Bio import SeqIO
from io import StringIO

with open("input.txt") as f:
    lines = f.read().split("\n")
    q, p = lines[0].split(" ")
    q = int(q)
    p = int(p) / 100
    fastq = "\n".join(lines[1:])

seqs = SeqIO.parse(StringIO(fastq), "fastq")
good_sequences = 0
for seq in seqs:
    good_bases = 0
    for score in seq.letter_annotations["phred_quality"]:
        if score >= q:
            good_bases += 1
    if good_bases / len(seq) >= p:
        good_sequences += 1

print(good_sequences)