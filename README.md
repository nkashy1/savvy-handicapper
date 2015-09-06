# The Savvy Handicapper

The Handicapper has just learned a new game. He's not very good at it at the moment, but he gets better every time he
plays. He has to come up with a scheme to estimate his skill at the game so that he can offer people odds on his games
which are appropriate to his chances of winning.

- - -

This is just a fun little example of a Bayesian inference which runs pretty quickly without using any fancy distributional
assumptions on the priors and posteriors in question.

- - -

### The game and records

The game that the Handicapper is playing only has two possible outcomes. If the Handicapper wins a session of the game,
the result is recorded with a `1`, and if he loses it is recorded with a `0`.

The `resources/records` directory contains some sample series of records that can be used for analysis. Each records file
contains some number of lines with each line representing a game result and therefore either containing a `0` or a `1`.

There are two scripts that you may use to generate records:

1. `fixed_prob_records.py` -- writes to a given `outfile` a series of `n` records with each record being a `1` with probability `p` and `0` otherwise.
To run this script:
```
$ python fixed_prob_records.py p n outfile
```

2. `logistic_increasing_records.py` -- writes to a given `outfile` a series of `n` records with the first record being generated
with probability equal to the value of the logistic function at `initial_param` and with this probability being increased every
`change_rate` samples by adding `epsilon` to the current logistic parameter. To run this script:
```
$ python logistc_increasing_records initial_param epsilon n change_rate outfile
```

- - -

### Analysis

The Handicapper figures that his skill at any given time can be quantified as the probability of him winning the next game that he plays.
Assuming the existence of this probability, he chooses the following estimation scheme -- He only cares about estimating his
probability of success to within 0.1 % and so he divides the interval `[0, 1]` into thousandths and simply estimates using
Bayes rule how likely it is, given his results so far, that his probability of success is `j/1000` for each `0 <= j <= 1000`.

In order to run an analysis:
```
$ python handicap.py records
```
where `records` is the location of the file of records you would like to use in an analysis. When you call the analysis
script in this manner, the Handicapper assumes a uniform prior distribution on the probabilities `j/1000`, for `0 <= j <= 1000`.

You can specify a prior using the optional `--statsfile` argument, which points to a file representing a custom prior distribution. This
file should contain exactly 1001 lines with line `j` being the prior probability of the Handicapper's probability of winning the game being
`j/1000`.

- - -

