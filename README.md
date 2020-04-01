
# fasta2png

[![Build Status](https://travis-ci.com/metebalci/fasta2png.svg?branch=master)](https://travis-ci.com/metebalci/fasta2png)

This package includes two programs:

- fna2png: generates PNG images from nucleic acid (na) sequences in FASTA format representing nucleic acids with different colors.
- faa2png: generates PNG images from amino acid (aa) / protein sequences in FASTA format representing amino acids (codons) with different colors.

Both programs scan the sequence and generates a (small) rectangle (configurable size with --pixel-size) for each nucleotide bases or for each amino acids (codons) from top-left to bottom-right. The aspect ratio of the PNG is also configurable (with --aspect-ratio). The PNG image is in RGBA format.

For nucleic acid outputs, A, C, G, T is painted using different colors (U is same as T), and all other codes (N and others) are painted with white. The background of the image (meaning the remaining area in the image) is painted with black. These colors are also configurable.

For amino acid (codon) outputs, each codon is painted using a different color. The gap (-) is painted as same as background. Only the background color is configurable, because there are so many (27) codes.

# Installation

```
pip install fasta2png
```

# Usage: fna2png

```
fna2png --input <fna_input_in_fasta_format> --output <output_filename_of_png>
```

There are various options to customize PNG output, see help `fna2png --help` for more info.

# Usage: faa2png

```
faa2png --input <faa_input_in_fasta_format> --output <output_filename_of_png>
```

There are some options to customize PNG output, see help `faa2png --help` for more info.

# Example: fna2png

[NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512) is the SARS-CoV-2 (corona virus 2) complete genome sequenced by Chinese researchers in January 2020.

NC_045512.2.fna file below is https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta&log$=seqview&format=text.

```
$ fna2png --input NC_045512.2.fna --output NC_045512.2.png --pixel-size 8 --aspect-ratio 3 2

seqdesc: NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
seqlen: 29903
```

![NC_045512.2.fna.png](NC_045512.2.fna.png)

# Example: faa2png

This example is using the same SARS-CoV-2 sequence, but taking the protein encoded by the first gene in its genome called ORF1ab.

YP_009724389.1.faa file below is https://www.ncbi.nlm.nih.gov/protein/YP_009724389.1?report=fasta&log$=seqview&format=text.

```
$ faa2png --input YP_009724389.1.faa --output YP_009724389.1.faa.png --pixel-size 4 --aspect-ratio 3 2

seqdesc: YP_009724389.1 orf1ab polyprotein [Severe acute respiratory syndrome coronavirus 2]
seqlen: 7096
```

![YP_009724389.1.faa.png](YP_009724389.1.faa.png)
