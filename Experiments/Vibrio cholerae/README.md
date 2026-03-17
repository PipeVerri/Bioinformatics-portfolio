# Vibrio cholerae Genomic Analysis

This directory contains computational experiments focused on the genomic analysis of *Vibrio cholerae*, specifically aiming to identify functional regions and patterns within its DNA sequence.

## Notebooks

- **[frequent_k-mer_finding.ipynb](./frequent_k-mer_finding.ipynb)**: 
  Analysis of overrepresented 9-mers in the first chromosome. It uses frequent word counting to identify potential regulatory motifs and calculates the statistical probability of these occurrences.

- **[oriC_finding.ipynb](./oriC_finding.ipynb)**: 
  Search for the Origin of Replication (*oriC*). This experiment combines:
  - **GC Skew Analysis**: Mapping the cumulative $C-G$ skew to find the minimum point where replication typically begins.
  - **DnaA Box Identification**: Searching for the `TTATCCACA` motif (and its variants with Hamming distance $\leq 1$) in the proximity of the `dnaA` gene and the skew minimum.

## Data
The analysis uses *Vibrio cholerae* genomic data (FASTA) and annotations (GFF) [sourced from the RefSeq database](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_008369605.1/).