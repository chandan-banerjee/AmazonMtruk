import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/nandikabanerjee/AI/AmazonMtruk/mod5_mtruk/assignment5_1_starter/data/coupons.csv')

print(data.head())

# What proportion of the total observations chose to accept the coupon?
proportion_accepted = data['Y'].mean()
print(f"Proportion of observations that accepted the coupon: {proportion_accepted:.2f}")

# new changes