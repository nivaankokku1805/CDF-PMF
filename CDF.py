import scipy.stats as stats

prob = 1 - stats.binom.cdf(6, 10, 0.5)
print("Probability of getting more than 6 heads in ten coin flips is:", prob)