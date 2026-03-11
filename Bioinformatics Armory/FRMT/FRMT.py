from Bio import Entrez
import time

Entrez.email = "pipe.verri@gmail.com"
ids = input().split(" ")
smallest = None

for i in ids:
    stream = Entrez.efetch(db="nucleotide", id=i, rettype="fasta")
    fasta = stream.read()
    if smallest is None:
        smallest = fasta
    elif len(smallest) > len(fasta):
        smallest = fasta
    time.sleep(0.5)
    print(f"Read {i}")

with open("output.txt", "w") as f:
    f.write(smallest)