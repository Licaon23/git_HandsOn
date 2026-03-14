# Sequence Classifier Script

This Python script classifies an input nucleotide sequence as DNA, RNA, both possible, or neither. It can also optionally search for a motif inside the sequence.

## Purpose

The script is designed to:

- read a sequence from the command line
- check whether it contains only valid nucleotide characters
- determine whether it is DNA or RNA
- optionally search for a motif within the sequence

## Code overview

The script uses three main modules:

- `sys` to inspect command-line arguments and exit when needed
- `re` to validate the sequence and search for motifs using regular expressions
- `argparse` to define and parse command-line arguments

## Full behavior

### 1. Shebang line

```python
#!/usr/bin/env python
```

This tells the shell to run the script with the Python interpreter available in the user's environment.

---

### 2. Imports

```python
import sys, re
from argparse import ArgumentParser
```

These lines import the required modules:

- `sys` gives access to command-line arguments through `sys.argv`
- `re` enables regular expression matching
- `ArgumentParser` is used to define and handle command-line options

---

### 3. Create the argument parser

```python
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
```

This creates a parser object and provides a short description of the script.

---

### 4. Define command-line arguments

```python
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
```

The script accepts:

- `-s` or `--seq`: the input sequence, required
- `-m` or `--motif`: an optional motif to search in the sequence

---

### 5. Show help if no arguments are provided

```python
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
```

If the script is run without any arguments, it prints the help message and exits with status code `1`.

---

### 6. Parse arguments

```python
args = parser.parse_args()
```

This reads the command-line arguments and stores them in the `args` object.

---

### 7. Convert sequence to uppercase

```python
args.seq = args.seq.upper()
```

This ensures the sequence is handled case-insensitively.

For example:

- `acgt`
- `ACGT`
- `AcGt`

will all be treated the same way.

---

### 8. Validate sequence characters

```python
if re.search('^[ACGTU]+$', args.seq):
```

This regular expression checks whether the sequence contains only valid nucleotide characters:

- `A`
- `C`
- `G`
- `T`
- `U`

Explanation of the regex:

- `^` = start of string
- `[ACGTU]` = allowed characters
- `+` = one or more characters
- `$` = end of string

So the whole sequence must consist only of these letters.

---

### 9. Classify the sequence

#### If it contains `T`

```python
if re.search('T', args.seq):
    print ('The sequence is DNA')
```

If the sequence includes `T`, it is classified as DNA.

#### Else if it contains `U`

```python
elif re.search('U', args.seq):
    print ('The sequence is RNA')
```

If it contains `U` and not `T`, it is classified as RNA.

#### Else

```python
else:
    print ('The sequence can be DNA or RNA')
```

If it contains only `A`, `C`, and `G`, then it could belong to either DNA or RNA.

---

### 10. Handle invalid sequences

```python
else:
    print ('The sequence is not DNA nor RNA')
```

If the sequence contains any invalid character, such as numbers or other letters, it is rejected.

Examples of invalid sequences:

- `ABCD`
- `ACGTX`
- `12345`

---

### 11. Optional motif search

```python
if args.motif:
```

If the user provides a motif, the script performs a motif search.

#### Convert motif to uppercase

```python
args.motif = args.motif.upper()
```

This allows case-insensitive matching between motif and sequence.

#### Print a search message

```python
print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
```

This prints a message before performing the search.

The `end=''` argument prevents a newline so the result can appear on the same line.

#### Search for the motif

```python
if re.search(args.motif, args.seq):
    print("FOUND-yai!")
else:
    print("NOT FOUND-bad luck...")
```

If the motif is found in the sequence, the script prints:

```text
FOUND-yai!
```

Otherwise it prints:

```text
NOT FOUND-bad luck...
```

---

## Usage

Run the script from the command line like this:

```bash
python seqClass.py -s ACGT
```

Or, if the file is executable:

```bash
./seqClass.py -s ACGT
```

### With motif search

```bash
python seqClass.py -s ACGTACGT -m GTA
```

---

## Example outputs

### Example 1: DNA sequence

```bash
python seqClass.py -s ACTGTT
```

Output:

```text
The sequence is DNA
```

### Example 2: RNA sequence

```bash
python seqClass.py -s ACUGUU
```

Output:

```text
The sequence is RNA
```

### Example 3: Could be DNA or RNA

```bash
python seqClass.py -s ACGGCA
```

Output:

```text
The sequence can be DNA or RNA
```

### Example 4: Invalid sequence

```bash
python seqClass.py -s ACGTXA
```

Output:

```text
The sequence is not DNA nor RNA
```

### Example 5: Motif found

```bash
python seqClass.py -s ACGTACGT -m TAC
```

Output:

```text
The sequence is DNA
Motif search enabled: looking for motif "TAC" in sequence "ACGTACGT"... FOUND-yai!
```

### Example 6: Motif not found

```bash
python seqClass.py -s ACGTACGT -m AAA
```

Output:

```text
The sequence is DNA
Motif search enabled: looking for motif "AAA" in sequence "ACGTACGT"... NOT FOUND-bad luck...
```

---

## Notes

### DNA/RNA logic

The script assumes:

- sequences containing `T` are DNA
- sequences containing `U` are RNA
- sequences with neither `T` nor `U` could be either

It does not explicitly handle sequences that contain both `T` and `U`. In that case, the current logic will classify them as DNA because it checks for `T` first.

### Motif matching uses regular expressions

The motif search uses:

```python
re.search(args.motif, args.seq)
```

This means the motif is interpreted as a regular expression, not just plain text.

For example:

- `A.G` would match any three-character pattern starting with `A` and ending with `G`
- `A*` has special regex behavior

If you want literal motif matching only, the motif should be escaped or a plain substring search should be used instead.

---

## Summary

This script is a simple command-line tool that:

1. reads a nucleotide sequence
2. validates its characters
3. classifies it as DNA, RNA, both possible, or invalid
4. optionally searches for a motif

It is useful as a small bioinformatics practice script for learning:

- Python scripting
- argument parsing with `argparse`
- regular expressions with `re`
- basic sequence classification logic
