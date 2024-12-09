import pandas as pd
from scipy.stats import pearsonr

# Data creation
data = {'Variable_A': [1, 2, 3, 4, 5, 6], 'Variable_B': [2, 3, 4, 5, 6, 7]}
df = pd.DataFrame(data)

# Pearson correlation
correlation, _ = pearsonr(df['Variable_A'], df['Variable_B'])
print("Correlation between Variable_A and Variable_B:", correlation)

# Joint probability
joint_prob = len(df[(df['Variable_A'] == 3) & (df['Variable_B'] == 4)]) / len(df)
print("Joint probability P(A=3 and B=4):", joint_prob)

# Marginal probability
marginal_prob_A = len(df[df['Variable_A'] == 3]) / len(df)
print("Marginal probability P(A=3):", marginal_prob_A)

marginal_prob_B = len(df[df['Variable_B'] == 4]) / len(df)
print("Marginal probability P(B=4):", marginal_prob_B)

# Conditional probability
cond_prob = joint_prob / marginal_prob_B if marginal_prob_B != 0 else 0
print("Conditional probability P(A=3 | B=4):", cond_prob)
