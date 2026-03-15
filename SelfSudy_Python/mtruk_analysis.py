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

proportion_accepted_bar_coupons = data[data['coupon'] == 'Bar']['Y'].value_counts(normalize=True).get(1, 0)
print(f"Proportion of bar coupons accepted: {proportion_accepted_bar_coupons:.2f}")

portion_bar_acccepsted = data.query('coupon == "Bar" & Y == 1')
fraction_of_tot_bar =  portion_bar_acccepsted.shape[0]/ data.query('coupon == "Bar"').shape[0]
print(f"Interms of percentage of bar coupons accepted: {fraction_of_tot_bar:.2%}")