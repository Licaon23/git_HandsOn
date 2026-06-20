#!/usr/bin/env python

import sys
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Compute nucleotide percentages in a DNA sequence')

parser.add_argument("-s", "--seq", type = str, required = True, help = "Input DNA sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()

if all(base in "ACGT" for base in args.seq):

    print("The sequence is DNA")

    total_length = len(args.seq)

    a_percentage = args.seq.count("A") / total_length * 100
    c_percentage = args.seq.count("C") / total_length * 100
    g_percentage = args.seq.count("G") / total_length * 100
    t_percentage = args.seq.count("T") / total_length * 100

    print("A:", round(a_percentage, 2), "%")
    print("C:", round(c_percentage, 2), "%")
    print("G:", round(g_percentage, 2), "%")
    print("T:", round(t_percentage, 2), "%")

else:
    print("Invalid DNA sequence")
