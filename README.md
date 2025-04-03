
# fasta2png

[![CircleCI](https://circleci.com/gh/metebalci/fasta2png/tree/master.svg?style=svg)](https://circleci.com/gh/metebalci/fasta2png/tree/master)

This package includes two programs:

- `fna2png`: generates PNG images from nucleic acid (na) / nucleotide sequences in FASTA format representing different nucleic acids with different colors.

- `faa2png`: generates PNG images from amino acid (aa) / protein sequences in FASTA format representing different amino acids (codons) with different colors.

Both programs scan the file and generate an image containing solid squares (configurable size with `--pixel-size`) for each nucleotide bases or for each amino acids (codons) from top-left to bottom-right. The aspect ratio of the PNG is configurable (with `--aspect-ratio`). The PNG image is in RGBA format.

For nucleotide sequences, A, C, G, T is painted using different colors (U is same as T), and all other codes (N and others) are painted with white. The background of the image (meaning the remaining area in the image) is painted with black. These colors are also configurable.

For protein sequences, each amino acid/codon is painted using a different color. The gap (-) is painted as same as background. Only the background color is configurable, because there are so many (27) codes.

For nucleotide sequences, multi-FASTA format accepted and either a single image containing the (sequentially) combined sequence or one image for each sequence is generated. This is controlled with `--multi-mode` option.

For protein sequqnces, multi-FASTA format is not supported at the moment, an image only for the first sequence will be generated. If you require this feature, please create an issue.

# Installation

```
pip install fasta2png
```

# multi-FASTA format options

For fna files, `--multi-mode` can be set to:

- `f` or `first`: only processes the first sequence (ignores the multi-FASTA format)
- `c` or `combined`: creates a single image containing all sequences combined
- `s` or `separate`: creates one image for each sequence

# output options

For fna files, `--output` is optional. If it is not given, the name/identifier in the file is used as the output file name (with `.png` suffix automatically added).

If a multi-FASTA file is given with `--multi-mode=s`:

- if `--output` is given, it is used as a prefix, and file names are formed as `<prefix><seqnum>.png`, and `<seqnum>` starts from 1. 

- if `--output` is not given, the name/identifier of the sequence is used and only `.png` is added.

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

This example is using the same SARS-CoV-2 sequence, but taking the sequence of the protein encoded by the first gene in its genome called ORF1ab.

YP_009724389.1.faa file below is https://www.ncbi.nlm.nih.gov/protein/YP_009724389.1?report=fasta&log$=seqview&format=text.

```
$ faa2png --input YP_009724389.1.faa --output YP_009724389.1.faa.png --pixel-size 4 --aspect-ratio 3 2

seqdesc: YP_009724389.1 orf1ab polyprotein [Severe acute respiratory syndrome coronavirus 2]
seqlen: 7096
```

![YP_009724389.1.faa.png](YP_009724389.1.faa.png)

# Changes

- v9: Pillow updated to 11.1.0. migrated to pyproject.toml.
- v8: Pillow updated to 9.3.0. multi-FASTA format supported for fna files.
- v7: Pillow updated to 9.1.1, CI config updated.
- v6: Pillow updated to 9.0.1.
- v5: Pillow updated to 8.2.0.
- v4: dont use.
- v3: Pillow updated to v8.0.1.
