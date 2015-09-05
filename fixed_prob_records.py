from __future__ import print_function
import numpy as np


# Script set-up
import argparse

parser = argparse.ArgumentParser(description="Generate a file of game records in which the Handicapper has a fixed probability of winning.")
parser.add_argument('prob', type=float)
parser.add_argument('num_records', type=int)
parser.add_argument('outfile', type=argparse.FileType('w'))

args = parser.parse_args()


# Heavy lifting
samples = np.random.uniform(size=args.num_records)
for result in (samples <= args.prob):
    print(str(int(result)), file=args.outfile)

