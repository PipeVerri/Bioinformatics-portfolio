from Bio import SeqIO
from io import StringIO
fastq = StringIO(input())
seq = SeqIO.parse(fastq, "fastq")