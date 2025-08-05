import random
import numpy as np

print("This simulation models the theoretical performance of a strategy assuming:\n\n" 
"1.) trades are independent events\n"
"2.) constant lot sizing\n"
"3.) constant risk reward ratio\n"
"4.) a known win rate\n")

risk_reward_ratio = float(input("Input normalized risk reward ratio:"))
win_rate = float(input("Input win rate %:"))/100
trades = int(input("Input number of trades:"))

def simulate_trade(risk_reward_ratio, win_rate):
    random_number = random.random()
    if random_number < win_rate:
        outcome = risk_reward_ratio
    else:
        outcome = -1 * (risk_reward_ratio/risk_reward_ratio)
    return outcome

simulations = 1000
sim_list = []
for sim in range(simulations):
    pnl_list = []
    pnl = 0

    for trade in range(trades):
        outcome = simulate_trade(risk_reward_ratio, win_rate)
        pnl = pnl + outcome
        pnl_list.append(pnl)
    sim_list.append(pnl_list[-1])

mean = np.mean(sim_list)
sigma = np.std(sim_list)
two_sigma = 2* sigma
lower_bound = float(mean - two_sigma)
upper_bound = float(mean + two_sigma)

print("-----------------------------------------------")
print(f"After 1,000 simulations we find that {trades} trades have a 95% chance of returning between:")
print(f"{lower_bound} and {upper_bound} risk units")
print(f"with a mean of {mean} risk units")



