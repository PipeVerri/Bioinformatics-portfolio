from Bio import Entrez
Entrez.email = "pipe.verri@gmail.com"
stream = Entrez.esearch(db="nucleotide", term="Anthoxanthum[Organism] AND 2003/7/25:2005/12/27[PDAT]")
records = Entrez.read(stream)
print(records["Count"])