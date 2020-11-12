# SlotMachineSimulation
Simple python script that simulates running a basic slot machine for 1M experiments, and returns the percentage of experiments that won over $500.

Starts with $100.
Each set of 1M experiments breaks the $100 into 1 or more bets.
i.e. First run 1M experiments with 1 bet of $100.  Next run 1M experiments with 2 bets of $50, etc.

For each set of experiments, calculate the percentage of experiments that win $500 or more.

Results:
numberOfBets, DollarsPerBet, Percentage of experiments that makes over $500
