from __future__ import print_function
import numpy as np


# Script set-up
import argparse
import sys

parser = argparse.ArgumentParser(description="Estimate the Handicapper's skill at his game.")
parser.add_argument('--statsfile')
parser.add_argument('records', type=argparse.FileType('r'))
parser.add_argument('--outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('-s', type=int)

args = parser.parse_args()

if args.statsfile is None:
    significant_digits = 3
    if args.s is not None:
        significant_digits = args.s
    num_candidates = 1 + 10**significant_digits
    distribution = (1/float(num_candidates))*np.ones(num_candidates, dtype=float)
else:
    with open(args.statsfile, 'r') as statsfile:
        lines = list(statsfile)
    significant_digits = int(lines[0])
    distribution = np.array(lines[1:], dtype=float)


# Heavy lifting
from Estimator import Estimator

estimator = Estimator(distribution)
records = list(args.records)

for record in records:
    estimator.update(record)

if args.statsfile is not None:
    estimator.save(statsfile)

print(str(estimator.expectation()), file=args.outfile)