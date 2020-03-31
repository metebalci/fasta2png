
# fasta2png

[![Build Status](https://travis-ci.com/metebalci/fasta2png.svg?branch=master)](https://travis-ci.com/metebalci/fasta2png)

This program generates PNG images from nucleic acid (na) sequences in FASTA format.

It scans the sequence and generates a (small) rectangle (configurable size with --pixel-size) for each nucleotide bases from top-left to bottom-right. The aspect ratio of the PNG is also configurable (with --aspect-ratio). The PNG image is in RGBA format.

A, C, G, T is painted using different colors (U is same as T), and all other codes (N and others) are painted with white. The background of the image (meaning the remaining area in the image) is painted with black. These colors are also configurable.

# Installation

```
pip install fasta2png
```

# Usage

```
fna2png --input <input_in_fasta_format> --output <output_filename>
```

There are various options to customize PNG output, see help `fna2png --help` for more info.

# Example

[NC_045512.2](https://www.ncbi.nlm.nih.gov/nuccore/NC_045512) is the SARS-CoV-2 (corona virus 2) complete genome sequenced by Chinese researchers in January 2020.

NC_045512.2.fna file below is https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2?report=fasta&log$=seqview&format=text.

```
$ fna2png --input NC_045512.2.fna --output NC_045512.2.png --pixel-size 4 --aspect-ratio 3 2

seqdesc: NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
seqlen: 29903
```

![NC_045512.2.png](NC_045512.2.png)
