import pandas as pd
import numpy as np
from scipy.stats import pearsonr


data = {
    'Variable_A': [1, 2, 3, 4, 5, 6],
    'Variable_B': [2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(data)


def calculate_correlation(df, col1, col2):
    correlation, _ = pearsonr(df[col1], df[col2])
    return correlation

def joint_probability(df, event_A, event_B):
    joint_df = df[(df['Variable_A'] == event_A) & (df['Variable_B'] == event_B)]
    joint_prob = len(joint_df) / len(df)
    return joint_prob

def marginal_probability(df, event, variable):
    marginal_df = df[df[variable] == event]
    marginal_prob = len(marginal_df) / len(df)
    return marginal_prob

def conditional_probability(df, event_A, event_B):
    joint_prob = joint_probability(df, event_A, event_B)
    marginal_prob_B = marginal_probability(df, event_B, 'Variable_B')
    if marginal_prob_B == 0:
        return 0
    return joint_prob / marginal_prob_B


correlation = calculate_correlation(df, 'Variable_A', 'Variable_B')
print("Correlation between Variable_A and Variable_B:", correlation)


joint_prob = joint_probability(df, 3, 4)
print("Joint probability P(A=3 and B=4):", joint_prob)


marginal_prob_A = marginal_probability(df, 3, 'Variable_A')
print("Marginal probability P(A=3):", marginal_prob_A)

marginal_prob_B = marginal_probability(df, 4, 'Variable_B')
print("Marginal probability P(B=4):", marginal_prob_B)

cond_prob = conditional_probability(df, 3, 4)
print("Conditional probability P(A=3 | B=4):", cond_prob)
