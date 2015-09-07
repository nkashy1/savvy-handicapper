import numpy as np


class BetaEstimator(object):
    def __init__(self, alpha=1, beta=1):
        self.alpha = float(alpha)
        self.beta = float(beta)

    def update(self, record):
        record = int(record)
        self.alpha += record
        self.beta += 1 - record

    def batch_update(self, wins, losses):
        self.alpha += wins
        self.beta += losses

    def sample(self):
        return np.random.beta(self.alpha, self.beta)

    def expectation(self):
        return self.alpha/(self.alpha + self.beta)



# TESTS
import unittest

class BetaEstimatorTest(unittest.TestCase):
    def setUp(self):
        self.alpha = 1
        self.beta = 2
        self.estimator = BetaEstimator(self.alpha, self.beta)

    def test_constructor(self):
        estimator = self.estimator
        self.assertEqual(estimator.alpha, self.alpha)
        self.assertEqual(estimator.beta, self.beta)

    def test_update_win(self):
        estimator = self.estimator
        record = 1
        estimator.update(record)
        self.assertEqual(estimator.alpha, self.alpha+1)
        self.assertEqual(estimator.beta, self.beta)

    def test_update_loss(self):
        estimator = self.estimator
        record = 0
        estimator.update(record)
        self.assertEqual(estimator.alpha, self.alpha)
        self.assertEqual(estimator.beta, self.beta+1)

    def test_expectation(self):
        estimator = self.estimator
        self.assertEqual(estimator.expectation(), estimator.alpha/(estimator.alpha + estimator.beta))

    def test_batch_update(self):
        estimator = self.estimator
        wins = 100
        losses = 7
        estimator.batch_update(wins, losses)
        self.assertEqual(estimator.alpha, self.alpha+wins)
        self.assertEqual(estimator.beta, self.beta+losses)
