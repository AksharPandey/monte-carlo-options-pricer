

A Python Monte Carlo pricer for European call and put options. It simulates stock price paths with geometric Brownian motion (GBM) under risk-neutral drift, then discounts the average payoff to estimate the option price. Volatility can be estimated from real historical data.

Built as a learning project to connect stochastic modelling to derivatives pricing.

## Features
- Simulates stock price paths with GBM using the risk-free rate as drift (risk-neutral pricing)
- Prices European calls and puts as the discounted average payoff
- Estimates annualized historical volatility from daily log returns via `yfinance`, with a user-chosen window
- Plots sample price paths and the distribution of final prices

## How it works
1. Download historical prices for a ticker and compute daily log returns
2. Take the sample standard deviation and scale by √252 to get annualized volatility
3. Simulate price paths: each step adds a drift term `(r - σ²/2)·dt` and a random shock `σ·√dt·Z`
4. Compute the payoff at each path's final price, average across paths, and discount by `e^(-rT)`

The output is an estimate. It changes slightly between runs because the shocks are random, and the error shrinks with the square root of the number of simulations.

## Example output
- Inputs: K = 330 | T = 1 yr | r = [rate] | steps = 252 | sims = 10,000 | [call/put] on [ticker]
- Volatility estimated from [window] of historical data

<img width="1115" height="649" alt="Screenshot 2026-09-29 231211" src="https://github.com/user-attachments/assets/9f4edf65-fefc-4ebc-80ca-56d78277e37b" />

<img width="2167" height="1255" alt="image" src="https://github.com/user-attachments/assets/26082bae-10bd-482b-9034-88e1c6fafb14" />


## Requirements
numpy, matplotlib, yfinance (plus pandas if you use it in `Vol_calc.py`)

## Files
- `Monte Carlo Options Pricing.py`: main pricer
- `Vol_calc.py`: historical volatility estimator

## Limitations
- Assumes constant volatility and GBM (no jumps, no volatility smile)
- Historical volatility describes the past and is only an estimate of future volatility
- European options only; the price is not compared against a closed-form solution yet

## Planned
- Validate against the Black-Scholes formula
- Add standard error and confidence intervals
- Price path-dependent options (Asian, barrier)
