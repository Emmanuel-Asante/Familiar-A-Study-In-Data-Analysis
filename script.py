# Import libraries
import pandas as pd
import numpy as np
import math

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# Print out the first five rows of "lifespans" dataframe
print(lifespans.head())

# Save life spans of subscribers to the "vein" pack into a variable called vein_pack_lifespans
vein_pack_lifespans = lifespans.lifespan[lifespans.pack == "vein"]

# Calculate the average lifespan for Vein Pack subscribers
print(np.mean(vein_pack_lifespans))

# Round the average lifespans for Vein Pack subscribers
print("\nThe calculated average lifespans for Vein Pack subscribers: {} years\n".format(math.floor(np.mean(vein_pack_lifespans))))

# Import module that will be used for one sample t-test
from scipy.stats import ttest_1samp

# Run one sample t-test, store p-value into a variable called pval
ttest, pval = ttest_1samp(vein_pack_lifespans, 73)

# Print out the p-value from the one sample t-test
print("ONE SAMPLE T-TEST: p-value is {}\n".format(pval))

# Interpret the result from the test
print("Using a significance threshold of 0.05, the p-value of {} indicates that the average lifespan of Vein Pack subscribers is significantly different from 73 years.\n".format(pval))

# From the dataset "lifespans", Get lifespans of Artery Pack subscribers data and save them as artery_pack_lifespans
artery_pack_lifespans = lifespans.lifespan[lifespans.pack=='artery']

# Calculate the average lifespan for Artery Pack subscribers
print("{}\n".format(np.mean(artery_pack_lifespans)))

# Round the average lifesoan for Artery Pack subscribers
print("The calculated average lifespan for Artery Pack subscribers is {} years\n".format(math.floor(np.mean(artery_pack_lifespans))))

# Import module that will be used for two sample t-test
from scipy.stats import ttest_ind

# Run two sample t-test for vein_pack_lifespans and artery_pack_lifespans. Save the p-value into a variable called pval
ttest, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

# Print out the p-value from the two sample t-test
print("TWO SAMPLE T-TEST: p-value is {}\n".format(pval))

# Interpret the result from the test
print("Using a significance threshold of 0.05, the p-value of {} indicates that the average lifespan of Vein Pack subscribers is not signicantly different from the average lifespan of an Artery subscriber.\n".format(pval))

# Print out the first 5 rows of the "iron" dataset
print(iron.head())

# Display a new line
print("\n")

# Create a contingency table of the pack and iron columns in the iron data. Save the result as Xtab
Xtab = pd.crosstab(iron.pack, iron.iron)

# Print out Xtab
print(Xtab)

# Import module that will be used for Chi-Square test
from scipy.stats import chi2_contingency

# Run Chi-Square test, save p-value in a variable called pval
chi2, pval, dof, expected = chi2_contingency(Xtab)

# Print out the p-value
print("\nCHI-SQUARE TEST: p-value is {}\n".format(pval))

# Interpret the result from the test
print("Since the p-value of {} is smaller than 0.05 (significance threshold), we can conclude that there is a significant association between pack and iron level.".format(pval))