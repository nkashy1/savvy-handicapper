from __future__ import print_function

# Script set-up
import argparse

parser = argparse.ArgumentParser(description="Estimate the Handicapper's skill at his game using a beta distribution to model his success probability.")
parser.add_argument('records', type=argparse.FileType('r'))
parser.add_argument('-a', type=float)
parser.add_argument('-b', type=float)
args = parser.parse_args()


# Heavy lifting
from BetaEstimator import BetaEstimator

alpha = 1
if args.a is not None:
    if args.a <= 0:
        raise ValueError('a must be a positive real number.')
    alpha = args.a

beta = 1
if args.b is not None:
    raise ValueError('b must be a positive real number.')
    beta = args.b

estimator = BetaEstimator(alpha, beta)
records = list(map(int, args.records))
wins = sum(records)
losses = len(records) - wins
estimator.batch_update(wins, losses)

print(estimator.expectation())