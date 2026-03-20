from pathlib import Path
from BCBio import GFF
from Bio import SeqIO
import os

GENOMES_DIR = Path(__file__).parents[2] / "data/gamma-b/filtered_genomes/ncbi_dataset/data"
GFF_SEARCH_KEYS = ("Name", "gene_biotype", "gene", "product")

def has_chromosome_oric_or_dnaa(annot):
    for feature in annot.features:
        for key in GFF_SEARCH_KEYS:
            if key in feature.qualifiers:
                for value in feature.qualifiers[key]:
                    if "dnaa" in value.lower() or "oric" in value.lower():
                        return True

    return False

def load_genome(genome_folder):
    files = os.listdir(GENOMES_DIR / genome_folder)
    if files[0].endswith(".fna") or files[0].endswith(".fasta"):
        fasta_path = GENOMES_DIR / genome_folder / files[0]
        gff_path = GENOMES_DIR / genome_folder / files[1]
    else:
        fasta_path = GENOMES_DIR / genome_folder / files[1]
        gff_path = GENOMES_DIR / genome_folder / files[0]

    sequences = SeqIO.parse(fasta_path, format="fasta")
    annotations = GFF.parse(gff_path)
    return sequences, annotations

for genome_folder in os.listdir(GENOMES_DIR):
    if not os.path.isdir(GENOMES_DIR / genome_folder):
        continue

    # Get the FASTA and GFF paths
    sequences, annotations = load_genome(genome_folder)
    for seq, annot in zip(sequences, annotations):
        if "chromosome" in seq.description:  # Filter the plasmids out
            if has_chromosome_oric_or_dnaa(annot):
                print("Found DnaA")

    break
