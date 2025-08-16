import random
import numpy as np
import matplotlib.pyplot as plt

print("This model uses a Monte Carlo simulation to estimate the profitability distribution of a strategy assuming:\n" 
"1.) trades are independent events\n"
"2.) a known win rate\n"
"3.) constant risk reward ratio\n"
"4.) constant lot sizing\n")

win_rate = float(input("Input win rate %:"))/100
risk_reward_ratio = float(input("Input normalized risk reward ratio:"))
risk = int(input("How much are you risking per trade in $:"))
trades = int(input("Input number of trades:"))

def simulate_trade(risk_reward_ratio, win_rate):
    random_number = random.random()
    if random_number < win_rate:
        outcome = risk_reward_ratio #you win one unit of risk * (normalized rr ratio)
    else:
        outcome = -1 #lose one unit of risk
    return outcome

simulations = 100000
sim_list = []
all_pnls = []
for sim in range(simulations):
    pnl_list = []
    pnl = 0

    for trade in range(trades):
        outcome = simulate_trade(risk_reward_ratio, win_rate)
        pnl = pnl + outcome
        pnl_list.append(pnl)
    sim_list.append(pnl_list[-1]) # appends the final PnL value of that simulation into sim_list 
    all_pnls.append(pnl_list)

mean = np.mean(sim_list)
sigma = np.std(sim_list)
two_sigma = 2* sigma
lower_bound = float(mean - two_sigma)
upper_bound = float(mean + two_sigma)

print("\n -------------------------------------------------------------------------------------------------- \n")
print(f"After {simulations:,} simulations we find that risking ${risk} over {trades} trades with a {risk_reward_ratio}R:R and {win_rate*100}% win rate, has a 95% chance of returning between:")
print(f"${lower_bound * risk:,} and ${upper_bound * risk:,}")
print(f"with a mean return of ${mean*risk:,}, and standard deviation of ${sigma * risk}")

indices = range(100) #plot the first 100 simulated trajectories
plt.figure(1)
plt.xlabel('Number of trades')
plt.ylabel('Profits ($)')
plt.title(f'Simulated Trajectories')
for idx in indices:
    # y = all_pnls[idx]
    y = [x * risk for x in all_pnls[idx]]
    x = range(len(all_pnls[idx]))
    plt.plot(x,y)

sim_list_profit = [q * risk for q in sim_list] #convert from risk units to profits
plt.figure(2)
plt.xlabel(f'Final Profits ($)')
plt.ylabel('Frequency')
plt.title(f'Profitability Distribution: \n {risk_reward_ratio}:1 Risk Reward, {win_rate*100}% Win Rate')
n, bins, patches = plt.hist(sim_list_profit, bins=100)
plt.axvspan(lower_bound * risk, upper_bound * risk, alpha=0.2, color='yellow') # Shade 95% region
plt.axvline(lower_bound * risk, color='red', linestyle='--', label='Lower bound') # Vertical lines for bounds
plt.axvline(upper_bound * risk, color='red', linestyle='--', label='Upper bound')
plt.axvline(mean * risk, color='blue', linestyle='-', label='Mean')

for i in range(len(patches)): # Highlight bins within bounds (change color)
    if bins[i] >= lower_bound * risk and bins[i+1] <= upper_bound * risk:
        patches[i].set_facecolor('blue')

plt.legend()
plt.show()

