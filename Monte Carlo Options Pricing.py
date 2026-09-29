import numpy as np
import matplotlib.pyplot as plt
import Vol_calc as V


K = float(input("Enter strike price: "))  # price to buy or sell
T = float(input("Enter time to expiration (Years): "))
r = float(input("Enter risk free rate: "))  # risk-free rate
ticker = input("Enter ticker: ")
period = input("Enter period (like 1mo, 1y, 1d): ")
vol = V.volfinder(ticker, period)
S0 = V.currentprice(ticker, period)
steps = int(input("Enter number of increments: "))
sims = int(input("Enter amount of simulations: "))
pc = input("Enter Put/Call Option: ")



dt = T/steps  # Time Per Step
drift = (r-(vol**2)/2)*dt  # Predictable Change


Sims = np.random.normal(0, 1, (sims,  steps)) * vol * np.sqrt(dt) + drift
# 2D list containing multiple simulations of price change

CumSum = np.exp(np.cumsum(Sims, axis=1)) * S0
#Cumulative Sum across time axis scaled across Current Stock Price

prices = CumSum[:, -1]
# Get an array of final price of all days

if pc.upper() == 'PUT':
    payoff = np.maximum(K - prices, 0)
elif pc.upper() == 'CALL':
    payoff = np.maximum(prices - K, 0)
else:
    print("Invalid Option provided, going with 'PUT'")
    payoff = np.maximum(K - prices, 0)

# Remove all non-negative values to 0, changes based on users input of Put or Call

print("The Option price is", np.mean(payoff) * np.exp(-r*T))
# Discount factor so -r * T is amount of discounting
plt.style.use('dark_background')
plt.plot(CumSum[:50, :].T)
plt.show()









