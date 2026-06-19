# Sequence Classifier Script

This Python script classifies an input nucleotide sequence as DNA, RNA, both possible, or neither. It can also optionally search for a motif inside the sequence.

## Purpose

The script is designed to:

- read a sequence from the command line
- check whether it contains only valid nucleotide characters
- determine whether it is DNA or RNA
- optionally search for a motif within the sequence

## Usage

Run the script from the command line like this:

```bash
python seqClass.py -s ACGT
```

### With motif search

```bash
python seqClass.py -s ACGTACGT -m GTA
```
