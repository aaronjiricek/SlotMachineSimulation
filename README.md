# SlotMachineSimulation
Simple python script that simulates running a basic slot machine for 1M experiments, and returns the percentage of experiments that won over $500.

Starts with $100.
Each set of experiments breaks the $100 into 1 or more bets.
i.e. experiment 1 runs 1M times with 1 bet of $100.  experiment 2 runs 1M times with 2 bets of $50, etc.
Results:
numberOfBets, DollarsPerBet, Percentage of experiments that makes over $500
