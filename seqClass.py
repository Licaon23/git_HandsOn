#!/usr/bin/env python
# Shebang line: tells the shell to run this script with the Python interpreter
# found in the user's environment.

import sys, re
# sys: used here to inspect command-line arguments and exit the program.
# re: regular expressions module, used to validate the sequence and search motifs.

from argparse import ArgumentParser
# Imports ArgumentParser, which helps define and parse command-line arguments.

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# Creates the argument parser object and sets a short description of the program.

parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
# Defines a required argument for the input sequence.
# The user can provide it as -s or --seq.
# type=str means the input will be treated as text.

parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
# Defines an optional argument for a motif to search inside the sequence.
# The user can provide it as -m or --motif.


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# If the script is run with no arguments at all, show the help message
# and exit with status code 1 to indicate incorrect usage.
    
args = parser.parse_args()
# Parses the arguments provided by the user and stores them in 'args'.


args.seq = args.seq.upper()
# Converts the sequence to uppercase so validation and searches are case-insensitive.



if re.search('^[ACGTU]+$', args.seq):
    # Checks whether the sequence contains only valid nucleotide letters:
    # A, C, G, T, or U.
    # ^ and $ mean the whole string must match.
    # + means one or more valid characters.

    if re.search('T', args.seq):
        print ('The sequence is DNA')
        # Checks whether the sequence contains only valid nucleotide letters:
    # A, C, G, T, or U.
    # ^ and $ mean the whole string must match.
    # + means one or more valid characters.

    elif re.search('U', args.seq):
        print ('The sequence is RNA')
        # If the sequence contains U (and not T, due to the previous condition),
        # it is classified as RNA.

        
    else:
        print ('The sequence can be DNA or RNA')
        # If the sequence contains only A, C, and G with neither T nor U,
        # it could belong to either DNA or RNA.
        
else:
    print ('The sequence is not DNA nor RNA')
    # If invalid characters are present, the sequence is not considered DNA or RNA.


if args.motif:
    # This block runs only if the user provided the optional motif argument.
    
    args.motif = args.motif.upper()
    # Converts the motif to uppercase so the search matches the uppercase sequence.
    
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    # Prints a message announcing the motif search.
    # end='' keeps the cursor on the same line so the result can be appended.
    
    if re.search(args.motif, args.seq):
        print("FOUND-yai!")
        # If the motif pattern is found anywhere in the sequence, print success.
        
    else:
        print("NOT FOUND-bad luck...")
        # If the motif is not found, print failure.
        
