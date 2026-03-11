from Bio import SeqIO
from io import StringIO

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    limit = int(lines[0])
    fastq = StringIO("\n".join(lines[1:]))

seqs = SeqIO.parse(fastq, "fastq")
count = 0
for seq in seqs:
    phred = seq.letter_annotations["phred_quality"]
    mean = sum(phred) / len(phred)
    if mean < limit:
        count += 1

print(count)