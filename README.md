# Bioinformatics Portfolio

A collection of bioiSimSnformatics experiments and competitive programming solutions focused on genomics, sequence analysis, and algorithmic problems.

## Experiments

This section contains in-depth genomic analyses, documented in Jupyter Notebooks.

- **[Vibrio cholerae](./Experiments/Vibrio%20cholerae/)**: 
  - Identification of the Origin of Replication (*oriC*) using cumulative GC skew.
  - Frequent k-mer (9-mer) analysis and statistical probability of regulatory motifs.
  - Search for DnaA boxes in the *V. cholerae* genome.

## Rosalind Solutions

Solutions to problems from the [Rosalind](https://rosalind.info/) platform, specifically focusing on the **Bioinformatics Armory** track.

- **[Bioinformatics Armory](./Rosalind/Bioinformatics%20Armory/)**: 
  - Scripts for processing FASTA files, GenBank records, and sequence alignments.
  - Implementations for common tools like `Biopython`, `EMBOSS`, and `NCBI Entrez`.

## Project Structure

```text
├── data/               # Genomic datasets (FASTA, GFF)
├── Experiments/        # Specialized research notebooks
├── Rosalind/           # Algorithm and tool practice (Rosalind.info)
└── utils/              # Custom library for sequence analysis (KmerFinder, SkewPlots)
```