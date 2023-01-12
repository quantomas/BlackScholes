
# @author: quantomas
# original code: The Python Quants


## Black-Scholes-Merton Option Pricing

# Libs
import numpy as np
np.set_printoptions(precision=5)

import math
from pylab import mpl, plt



S0 = 100
r = 0.05
sigma = 0.2
T = 1.0
# I = 10000
I = 1000000

# np.random.seed(100)

ST = S0 * np.exp((r - sigma ** 2 / 2) * T +
     sigma * math.sqrt(T) * np.random.standard_normal(I))


ST[:8].round(1)

ST.mean()
S0 * math.exp(r * T)


## Plot
# Im Intervall der Abweichung ± σ \pm \sigma vom Erwartungswert sind 68,27 % aller Messwerte zu finden

plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300 
mpl.rcParams['font.family'] = 'serif'
plt.figure(figsize=(10, 6))
plt.hist(ST, bins=1000, label='frequency');
# plt.hist(ST, bins=30, label='frequency');
plt.axvline(ST.mean(), color='r', label='mean')
plt.axvline(ST.mean() + ST.std(), color='y', label='sd up')
plt.axvline(ST.mean() - ST.std(), color='y', label='sd down')
# plt.title("Im Intervall der Abweichung ± \sigma vom Erwartungswert sind 68,27 % aller Messwerte zu finden")
plt.title(r'Im Intervall der Abweichung ± $\sigma$ vom Erwartungswert sind 68,27 % aller Messwerte zu finden')
plt.legend(loc=0);


plt.show()


# Call-Option, basierend auf simuliertem ST
K = 105

CT = np.maximum(ST - K, 0)
CT[:8].round(1)

C0 = math.exp(-r * T) * CT.mean()
C0



## Monte Carlo Simulation

np.set_printoptions(formatter= {'float_kind': lambda x: '%7.3f' % x})

# Parameter - Bsp. 1
S0 = 36.
r = 0.06
T = 1.0
sigma = 0.2


# Parameter - Bsp. 2
S0 = 1.
r = 0.8
T = 1.0
sigma = 0.4


# Simulating the Stock Price Process

M = 100
I = 50000
dt = T / M
dt


np.random.seed(100)

rn = np.random.standard_normal((M + 1, I))
rn.shape
rn.round(2)

S = np.zeros_like(rn)

S[0] = S0
S


for t in range(1, M + 1):
    S[t] = S[t - 1] * np.exp((r - sigma ** 2 / 2) * dt +
                           sigma * math.sqrt(dt) * rn[t])

S


# Plot

# t = np.arange(0, M + 1)

def f(x):
     return S0 * np.exp(r * x / M * T)


m_grid = np.arange(0, M + 1)
t_grid = T * m_grid / M
exp_val = S0 * np.exp(r * t_grid)


plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['savefig.dpi'] = 300
plt.figure(figsize=(10, 6))
plt.plot(S[:, :100]);
# plt.plot(S[:, 10:20]);
# plt.plot(t, f(t), 'r-', linewidth=3)
plt.plot(m_grid, exp_val, 'r-', linewidth=3)

plt.show()


# 
ST = S[-1]

plt.figure(figsize=(10, 6))
# plt.hist(ST, bins=35, color='b', label='frequency');
plt.hist(ST, bins=1000, color='b', label='frequency');
plt.axvline(ST.mean(), color='r', label='mean')
plt.axvline(ST.mean() + ST.std(), color='y', label='sd up')
plt.axvline(ST.mean() - ST.std(), color='y', label='sd down')
plt.legend(loc=0);

plt.show()


S0 * math.exp(r * T)
S[-1].mean()

