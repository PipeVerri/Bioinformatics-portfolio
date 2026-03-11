from Bio import SeqIO
seq = SeqIO.parse("input.fasta.txt", "fastq")
SeqIO.write(seq, "output.txt", "fasta")