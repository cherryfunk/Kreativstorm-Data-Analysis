# %%
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# %%

# Load the dataset from a CSV file
df = pd.read_csv('Birthweight_reduced_kg_R.csv')

# Clean the column names by removing extra spaces
df.columns = df.columns.str.strip()

# Displays the first 5 rows
print(df.head())  

# %%
## Q1. What is the mean birth weight for babies of non-smoking mothers?

# Filter for non-smoking mothers (smoker == 0)
non_smokers_df = df[df['smoker'] == 0]

# Calculate the mean birth weight for non-smoking mothers
mean_birthweight_non_smokers = non_smokers_df['Birthweight'].mean()

# Print the result
print(f"Mean birth weight for non-smoking mothers: {mean_birthweight_non_smokers:.2f} kg")

# %%
## Q2. What is the mean birth weight for babies of smoking mothers?

# Filter the dataset for smoking mothers (smoker == 1)
smokers_df = df[df['smoker'] == 1]

# Calculate the mean birth weight for babies of smoking mothers
mean_birthweight_smokers = smokers_df['Birthweight'].mean()

# Print the result
print(f"Mean birth weight for smoking mothers: {mean_birthweight_smokers:.2f} kg")

# %%
## Q3. What is the mean head circumference for babies of non-smoking mothers?

# Filter the dataset for non-smoking mothers (smoker == 0)
non_smokers_df = df[df['smoker'] == 0]

# Calculate the mean head circumference for babies of non-smoking mothers
mean_headcirc_non_smokers = non_smokers_df['Headcirc'].mean()

# Print the result
print(f"Mean head circumference for non-smoking mothers: {mean_headcirc_non_smokers:.2f} cm")

# %%
## Q4. What is the mean gestational age at birth for babies of smoking mothers?

# Filter the dataset for smoking mothers (smoker == 1)
smokers_df = df[df['smoker'] == 1]

# Calculate the mean gestational age for babies of smoking mothers
mean_gestation_smokers = smokers_df['Gestation'].mean()

# Print the result
print(f"Mean gestational age for smoking mothers: {mean_gestation_smokers:.2f} weeks")

# %%
## Q5. What is the maximum head circumference for babies of non-smoking mothers?

# Filter the dataset for non-smoking mothers (smoker == 0)
non_smokers_df = df[df['smoker'] == 0]

# Find the maximum head circumference for babies of non-smoking mothers
max_headcirc_non_smokers = non_smokers_df['Headcirc'].max()

# Print the result
print(f"Maximum head circumference for non-smoking mothers: {max_headcirc_non_smokers:.2f} cm")

# %%
## Q6. What is the minimum gestational age at birth for babies of smoking mothers?

# Filter the dataset for smoking mothers (smoker == 1)
smokers_df = df[df['smoker'] == 1]

# Find the minimum gestational age for babies of smoking mothers
min_gestation_smokers = smokers_df['Gestation'].min()

# Print the result
print(f"Minimum gestational age for smoking mothers: {min_gestation_smokers:.2f} weeks")

# %%
## Q7. Based on the dataset you have, out of the two, which one would be a better bet: "Pregnancy period in smoking mothers is shorter" or "Pregnancy period in non-smoking mothers is shorter"?

# Calculate the mean gestational age for smoking and non-smoking mothers
mean_gestation_smokers = smokers_df['Gestation'].mean()
mean_gestation_non_smokers = non_smokers_df['Gestation'].mean()

# Print both results for comparison
print(f"Mean gestational age for non-smoking mothers: {mean_gestation_non_smokers:.2f} weeks")
print(f"Mean gestational age for smoking mothers: {mean_gestation_smokers:.2f} weeks")

# %%
## Q8. Justify the above choice in a few words.

# Print the conclusion
print("Thus, the pregnancy period is slightly shorter for smoking mothers compared to non-smoking mothers.\nTherefore, the statement \"Pregnancy period in smoking mothers is shorter\" would be the better bet based on this dataset.")

# %%
## Q9. What is the baby birth weight range for babies of smoking mothers?

# Calculate the minimum and maximum birth weight for babies of smoking mothers
min_birthweight_smokers = smokers_df['Birthweight'].min()
max_birthweight_smokers = smokers_df['Birthweight'].max()

# Calculate the range by subtracting the minimum from the maximum
birthweight_range_smokers = max_birthweight_smokers - min_birthweight_smokers

# Print the result
print(f"The birth weight range for babies of smoking mothers is {birthweight_range_smokers:.2f} kg")

# %%
# Calculate the minimum and maximum birth weight for babies of non-smoking mothers
min_birthweight_non_smokers = non_smokers_df['Birthweight'].min()
max_birthweight_non_smokers = non_smokers_df['Birthweight'].max()

# Calculate the range by subtracting the minimum from the maximum for non-smoking mothers
birthweight_range_non_smokers = max_birthweight_non_smokers - min_birthweight_non_smokers

# Print both ranges for comparison
print(f"Birth weight range for smoking mothers: {birthweight_range_smokers:.2f} kg")
print(f"Birth weight range for non-smoking mothers: {birthweight_range_non_smokers:.2f} kg")

interpretation = """
Interpretation:

The larger birth weight range for babies of smoking mothers (2.65 kg) compared to non-smoking mothers (1.90 kg) 
suggests that there is more variation in the birth weights of babies born to smoking mothers. 
This could indicate that smoking has a broader impact on birth weight, potentially causing greater deviations 
from the norm (both lower and higher weights).

In contrast, the birth weights of babies born to non-smoking mothers tend to be more consistent and within a 
narrower range, suggesting less variability and a more stable environment for fetal development.

This implies that smoking may contribute to greater uncertainty and potential risk in terms of birth weight outcomes.
"""

print(interpretation)


# %%
## Q11. Are head circumference data for babies of smoking mothers normally distributed?

# Filter the dataset for smoking mothers
smokers_df = df[df['smoker'] == 1]

# Extract head circumference data for smoking mothers
headcirc_smokers = smokers_df['Headcirc']

# 1. Visual Check: Plot histogram and Q-Q plot

# Histogram
plt.hist(headcirc_smokers, bins=10, edgecolor='k', alpha=0.7)
plt.title('Histogram of Head Circumference for Smoking Mothers')
plt.xlabel('Head Circumference (cm)')
plt.ylabel('Frequency')
plt.show()

# Q-Q Plot
stats.probplot(headcirc_smokers, dist="norm", plot=plt)
plt.title('Q-Q Plot of Head Circumference for Smoking Mothers')
plt.show()

# 2. Statistical Tests

# Shapiro-Wilk Test
shapiro_test = stats.shapiro(headcirc_smokers)
print(f'Shapiro-Wilk Test: Statistic={shapiro_test.statistic}, p-value={shapiro_test.pvalue}')

# Kolmogorov-Smirnov test comparing headcirc_smokers to a normal distribution
ks_test = stats.kstest(headcirc_smokers, 'norm', args=(headcirc_smokers.mean(), headcirc_smokers.std()))
print(f'Kolmogorov-Smirnov Test: Statistic={ks_test.statistic}, p-value={ks_test.pvalue}')

interpretation = """
Explanation:

    1. Histogram: A bell-shaped histogram indicates that the data may follow a normal distribution. 
    
        In this case, the histogram shows that most of the data points cluster around the mean, with a shape resembling the normal distribution curve.

    2. Q-Q Plot: The Q-Q (quantile-quantile) plot compares the quantiles of the sample data to the quantiles of a standard normal distribution. 
    
        If the data points align closely to the diagonal reference line, the data is likely normally distributed. \n
        In our case, the data points in the Q-Q plot fall closely along the straight line, providing visual evidence that the data may be normally distributed.

    3. Shapiro-Wilk Test: The Shapiro-Wilk test is a formal statistical test used to assess the normality of the data. 

        It computes a test statistic and a p-value. If the p-value is greater than 0.05, the null hypothesis (that the data is normally distributed) cannot be rejected. \n
        In our case, the Shapiro-Wilk test returned a p-value of 0.372, which is greater than 0.05, meaning that the data can be considered normally distributed.

    4. Kolmogorov-Smirnov (K-S) Test: The Kolmogorov-Smirnov test compares the empirical distribution of the data to a reference distribution (in this case, the normal distribution). 
        
        Similar to the Shapiro-Wilk test, it calculates a test statistic and p-value. A p-value greater than 0.05 suggests that the sample distribution does not differ significantly from the reference distribution. \n
        In our analysis, the K-S test returned a p-value of 0.820, which is well above the 0.05 threshold, indicating no significant deviation from normality.

Interpretation:

Since the p-value in both the Shapiro-Wilk test (0.372) and the Kolmogorov-Smirnov test (0.820) is greater than the common significance level of 0.05, we fail to reject the null hypothesis. This means that the head circumference data for babies of smoking mothers can be considered normally distributed.

Additionally, the histogram and Q-Q plot visually support this conclusion, as the data appears to follow a normal distribution. Thus, both visual and statistical tests confirm that the data is consistent with a normal distribution.
"""
print(interpretation)

# %%
## Q12. What is the significance value for the above on the Shapiro-Wilk test?

# From the previous test run, the Shapiro-Wilk test for the head circumference data of smoking mothers returned a p-value of 0.372.

# %%
## Q13. What is the standard score (Z-score) for head circumference of 35.05 (X=35.05) in non-smoking mothers?

# Filter the dataset for non-smoking mothers (smoker == 0)
non_smokers_df = df[df['smoker'] == 0]

# Calculate the mean and standard deviation for head circumference of non-smoking mothers
mean_headcirc_non_smokers = non_smokers_df['Headcirc'].mean()
std_headcirc_non_smokers = non_smokers_df['Headcirc'].std()

# The value for which we want to calculate the Z-score
X = 35.05

# Calculate the Z-score
z_score = (X - mean_headcirc_non_smokers) / std_headcirc_non_smokers

# Print the Z-score result
print(f"The Z-score for head circumference of 35.05 cm is: {z_score:.2f} because the mean is {mean_headcirc_non_smokers:.2f} and the standard deviation is {std_headcirc_non_smokers:.2f}.")

# %%
## Q14. How are birth weight data of non-smoking mothers skewed?

# Calculate the skewness for birth weight data of non-smoking mothers
birthweight_skewness_non_smokers = stats.skew(non_smokers_df['Birthweight'])

# Print the result
print(f"The skewness of birth weight data for non-smoking mothers is: {birthweight_skewness_non_smokers:.2f}")

# %%
## Q15. Are birth weight data for babies of smoking mothers normally distributed?

# Filter the dataset for smoking mothers
smokers_df = df[df['smoker'] == 1]

# Extract birth weight data for smoking mothers
birthweight_smokers = smokers_df['Birthweight']

# 1. Visual Check: Plot histogram and Q-Q plot

# Histogram
plt.hist(birthweight_smokers, bins=10, edgecolor='k', alpha=0.7)
plt.title('Histogram of Birth Weight for Smoking Mothers')
plt.xlabel('Birth Weight (kg)')
plt.ylabel('Frequency')
plt.show()

# Q-Q Plot
stats.probplot(birthweight_smokers, dist="norm", plot=plt)

plt.title('Q-Q Plot of Birth Weight for Smoking Mothers')
plt.show()

# 2. Shapiro-Wilk Test
shapiro_test = stats.shapiro(birthweight_smokers)
print(f'Shapiro-Wilk Test: Statistic={shapiro_test.statistic}, p-value={shapiro_test.pvalue}')

interpretation = """
Since the p-value in the Shapiro-Wilk test is greater than the common significance level of 0.05, we fail to reject the null hypothesis. This means that the birth weight data for babies of smoking mothers can be considered normally distributed.

Additionally, the histogram and Q-Q plot visually support this conclusion, as the data appears to follow a normal distribution. Thus, both visual and statistical tests confirm that the data is consistent with a normal distribution.
"""
print(interpretation)

# %%
## Q16. What is the significance value for the above on the Shapiro-Wilk test?

# = Q12

# %%

## Q17. Based on the dataset you have, how confident can you be in saying that a baby's birth weight will be +/- 1 standard deviation from the mean?

#Calculate the mean and standard deviation of the birth weight
mean_birthweight = df['Birthweight'].mean()
std_birthweight = df['Birthweight'].std()

#Define the range (mean - std, mean + std)
lower_bound = mean_birthweight - std_birthweight
upper_bound = mean_birthweight + std_birthweight

# Calculate the proportion of data points that fall within this range
within_1_std = df[(df['Birthweight'] >= lower_bound) & (df['Birthweight'] <= upper_bound)]

# Proportion of data points within ±1 standard deviation
proportion_within_1_std = len(within_1_std) / len(df)

# Output the result
print(f"Proportion of birth weights within ±1 standard deviation: {proportion_within_1_std:.2%}")

interpretation = """
Approximately 69.05% of the birth weights in the dataset fall within ± 1 standard deviation from the mean. This is quite close to the expected 68% from the empirical rule, suggesting that the birth weights roughly follow a normal distribution.
"""

print(interpretation)


# %%
## Q18. Based on the dataset you have, what is the probability that the birth weight for a baby of a smoking mother will be less than 4.2 kg?

# Filter the dataset for smoking mothers
smoking_mothers = df[df['smoker'] == 1]

# Total number of babies born to smoking mothers
total_smoking_mothers = len(smoking_mothers)

# Count the number of babies with birth weight less than 4.2 kg
babies_less_than_4_2kg = smoking_mothers[smoking_mothers['Birthweight'] < 4.2]

# Calculate the probability
probability = len(babies_less_than_4_2kg) / total_smoking_mothers

# Output the result
print(f"Probability that the birth weight for a baby of a smoking mother is less than 4.2 kg: {probability:.4f}")


# %%
# Filter the dataset for non-smoking mothers
non_smoking_mothers = df[df['smoker'] == 0]

import matplotlib.pyplot as plt
import scipy.stats as stats

# Histogram
plt.figure(figsize=(10, 5))
plt.hist(non_smoking_mothers['Length'], bins=15, edgecolor='black', alpha=0.7)
plt.title('Histogram of Baby Lengths (Non-Smoking Mothers)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Q-Q plot
plt.figure(figsize=(10, 5))
stats.probplot(non_smoking_mothers['Length'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Baby Lengths (Non-Smoking Mothers)')
plt.show()

# Apply the Shapiro-Wilk test to the length of the babies
stat, p_value = stats.shapiro(non_smoking_mothers['Length'])

# Output the p-value result
print(f"P-value from the Shapiro-Wilk test: {p_value:.4f}")

interpretation = """
The p-value from the Shapiro-Wilk test for the length of babies born to non-smoking mothers is approximately 0.0704. Since this p-value is greater than 0.05, we fail to reject the null hypothesis, suggesting that the length data for babies of non-smoking mothers is normally distributed.

From the Q-Q plot, if the points closely follow the diagonal line, it suggests that the data is approximately normally distributed, which aligns with the results of the Shapiro-Wilk test.

"""

print(interpretation)


# %%
## Q20. What is the significance value for the above on the Shapiro-Wilk test?

p_value = 0.0704

# %%
## Q21. What is the standard score for the length of a baby of 48.5cm for non-smoking mothers?


# Mean and standard deviation for length of babies born to non-smoking mothers
mean_length = non_smoking_mothers['Length'].mean()
std_length = non_smoking_mothers['Length'].std()

# Given length
X = 48.5

# Calculate the Z-score
z_score = (X - mean_length) / std_length

# Output the result
print(f"Z-score for a baby length of 48.5 cm: {z_score:.4f}")

interpretation = """
The Z-score for a baby length of 48.5 cm among non-smoking mothers is approximately -1.01. This indicates that a baby with a length of 48.5 cm is about 1 standard deviation below the mean length for babies born to non-smoking mothers. 
"""

print(interpretation)


# %%
## Q22. Based on the dataset you have, what is the probability that the length of baby for non-smoking mothers will be more than 55 cm?

# Mean and standard deviation for length of babies born to non-smoking mothers
mean_length = non_smoking_mothers['Length'].mean()
std_length = non_smoking_mothers['Length'].std()

# Given length
X = 55

# Step 1: Calculate the Z-score for length = 55 cm
z_score = (X - mean_length) / std_length

# Step 2: Calculate the cumulative probability for the Z-score
cumulative_prob = stats.norm.cdf(z_score)

# Step 3: Calculate the probability that length > 55 cm
probability = 1 - cumulative_prob

# Output the result
print(f"Probability that the length of a baby for non-smoking mothers is more than 55 cm: {probability:.4f}")

interpretation = """
The probability that the length of a baby for non-smoking mothers is more than 55 cm is approximately 16.2715%.
"""

print(interpretation)


