from __future__ import print_function
import numpy as np


class Estimator(object):
    def __init__(self, distribution):
        scale = len(distribution)
        self.probability_values = np.arange(scale, dtype=float)/(scale-1)
        self.distribution = distribution
        self.ones = np.ones(self.distribution.shape, dtype=float)
        self.epsilon = 1.0/(100*scale)

    def update(self, record):
        record = int(record)
        if record == 1:
            dot = self.probability_values*self.distribution
            result = self.unzero(dot)
            self.distribution = result/result.sum()
        else:
            dot = (self.ones - self.probability_values)*self.distribution
            result = self.unzero(dot)
            self.distribution = result/result.sum()

    def unzero(self, probs):
        small = (probs < self.epsilon).astype(float)
        big = (probs >= self.epsilon).astype(float)
        return big*probs + self.epsilon*small

    def save(self, statsfile):
        with open(statsfile, 'w') as outfile:
            for p in list(self.distribution):
                print(str(p), file=outfile)

    def sample(self):
        cumsum = self.distribution.cumsum()
        uniform_sample = np.random.uniform()
        return np.argmin(cumsum >= uniform_sample)/(cumsum.size+1)

    def expectation(self):
        return (self.probability_values*self.distribution).sum()


# TESTS
import unittest

class EstimatorTest0(unittest.TestCase):
    def setUp(self):
        distribution = np.array([0.25, 0.25, 0.25, 0.25])
        self.estimator = Estimator(distribution)
        self.scale = len(distribution)

    def test_constructor(self):
        estimator = self.estimator

        expected_probability_values = np.array([0, 1, 2, 3], dtype=float)/3
        for j in range(self.scale):
            self.assertEqual(estimator.probability_values[j], expected_probability_values[j])

        expected_distribution = np.array([0.25, 0.25, 0.25, 0.25])
        for j in range(self.scale):
            self.assertEqual(estimator.distribution[j], expected_distribution[j])

        self.assertEqual(estimator.ones.size, 4)

    def test_update_win(self):
        estimator = self.estimator
        estimator.update(1)
        self.assertAlmostEqual(estimator.distribution[0], 0)
        self.assertAlmostEqual(estimator.distribution[1], 1.0/6)
        self.assertAlmostEqual(estimator.distribution[2], 1.0/3)
        self.assertAlmostEqual(estimator.distribution[3], 1.0/2)

    def test_update_loss(self):
        estimator = self.estimator
        estimator.update(0)
        self.assertAlmostEqual(estimator.distribution[3], 0)
        self.assertAlmostEqual(estimator.distribution[2], 1.0/6)
        self.assertAlmostEqual(estimator.distribution[1], 1.0/3)
        self.assertAlmostEqual(estimator.distribution[0], 1.0/2)
