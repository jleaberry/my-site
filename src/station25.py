import numpy as np

#rng = np.random.default_rng(seed=7)
#for n in [10, 100, 1_000, 10_000, 100_000]:
#    est = rng.binomial(1, 0.7, size=n).mean()
#    print(f"n = {n:>7,}   estimate = {est:.4f}")

# Simulate a Bernoulli(0.7): 1 with probability 0.7, else 0.
# One draw = one simulated "day" for our sunny-day variable.

#x = rng.binomial(1, 0.7)
#print(x)  # 1 or 0

#draws = rng.binomial(1, 0.7, size=10_000)   # 10,000 simulated days
#print(draws[:12])       # [1 0 1 1 0 0 0 1 1 1 0 1]
#print(draws.mean())     # 0.7058  <- our estimate of P(X = 1)


rng = np.random.default_rng(seed=11)
n = 100_000

# Node 1: is it a sunny day?      Sunny ~ Bernoulli(0.6)
sunny = rng.binomial(1, 0.79, size=n)

# Node 2: is it a high sales day (over 100 units)?
#   P(high | sunny) = 0.8,  P(high | not sunny) = 0.3
theta = np.where(sunny == 1, 0.6, 0.11)
high_sales = rng.binomial(1, theta)

print(high_sales.mean())  # ~0.60  = 0.6*0.8 + 0.4*0.3


from functools import partialmethod
import daft

class dag(daft.PGM):
    def __init__(self, *args, **kwargs):
        daft.PGM.__init__(self, *args, **kwargs)

    latNode = partialmethod(daft.PGM.add_node, scale=1.3, aspect=2.4,
                            fontsize=10, plot_params={"facecolor": "aliceblue"})
    detNode = partialmethod(daft.PGM.add_node, aspect=5.4, fontsize=9.25,
                            alternate=True, plot_params={"facecolor": "aliceblue"})

pgm = dag(dpi=300, alternate_style="outer")
pgm.latNode("sunny", "Sunny Day\n" + r"$X \sim Bernoulli(0.6)$", 1, 3.4, scale=1.5, aspect=3)
pgm.detNode("theta", "Chance of High Sales\n" + r"$\theta_X = 0.8$ if $X{=}1$, $0.3$ if $X{=}0$", 1, 2.2, scale=1.5, aspect=3.8)
pgm.latNode("high", "High Sales Day\n" + r"$Y \sim Bernoulli(\theta_X)$", 1, 1, scale=1.5, aspect=3)
pgm.add_edge("sunny", "theta")
pgm.add_edge("theta", "high")
pgm.show()

rng = np.random.default_rng(seed=3)
shows = rng.binomial(3, 0.9, size=100_000)  # passengers who showed, per flight
print((shows == 3).mean())                  # ~0.729



rng = np.random.default_rng(seed=15)
draws = rng.binomial(20, 0.61, size=100_000)
print((draws >= 14).mean())

rng = np.random.default_rng(seed=1)
draws = rng.binomial(8, 0.51, size=100_000)
print((draws == 4).mean())


rng = np.random.default_rng(seed=42)

N = 100_000

# Simulate whether it was sunny
sunny = rng.binomial(1, 0.60, size=N)

# Simulate whether the target was hit
hit = np.where(
    sunny == 1,
    rng.binomial(1, 0.79, size=N),  # sunny days
    rng.binomial(1, 0.11, size=N)   # not sunny days
)

# Estimate P(Sunny | Hit)
estimate = sunny[hit == 1].mean()

print(estimate)