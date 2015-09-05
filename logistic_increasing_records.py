from __future__ import print_function
import numpy as np


# Script set-up
import argparse

parser = argparse.ArgumentParser(description="Generate a file of game records in which the Handicapper has a fixed probability of winning.")
parser.add_argument('initial_param', type=float)
parser.add_argument('epsilon', type=float)
parser.add_argument('num_records', type=int)
parser.add_argument('change_rate', type=int)
parser.add_argument('outfile', type=argparse.FileType('w'))

args = parser.parse_args()


# Heavy lifting

def logistic(x):
    if x >= 0:
        z = np.exp(-x)
        return 1/(1 + z)
    z = exp(x)
    return z/(1 + z)

samples = []
current_param = args.initial_param
current_prob = logistic(current_param)
for j in range(args.num_records):
    if np.random.uniform() <= current_prob:
        samples.append(1)
    else:
        samples.append(0)
    if j % args.change_rate == 0:
        current_param += args.epsilon
        current_prob = logistic(current_param)

for result in samples:
    print(str(result), file=args.outfile)
