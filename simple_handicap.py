from __future__ import print_function
import numpy as np


# Script set-up
import argparse
import sys

parser = argparse.ArgumentParser(description="Estimate the Handicapper's skill at his game to within 0.1%.")
parser.add_argument('--statsfile')
parser.add_argument('records', type=argparse.FileType('r'))
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
from SimpleEstimator import SimpleEstimator

estimator = SimpleEstimator(distribution)
records = list(args.records)

for record in records:
    estimator.update(record)

print(estimator.expectation())
