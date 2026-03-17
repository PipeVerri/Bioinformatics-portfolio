from Bio import SeqIO

seqs = SeqIO.parse("input.fasta", "fasta")
counter = 0
for seq in seqs:
    if seq.seq == seq.seq.reverse_complement():
        counter += 1
print(counter)