#!/usr/bin/env python
# coding: utf-8

# Question1: Define the z-statistic and explain its relationship to the standard normal distribution. How is the 
# z-statistic used in hypothesis testing?

# A z-statistic (or z-score) measures how many standard deviations a data point is from the mean of a distribution. Mathematically, the z-statistic is given by:
# 
# z=  σ / X−μ
# 
# Where:
# 
# X = the observed data value
# μ = the population mean
# σ = the population standard deviation
# 
# In the context of a sample mean, the formula becomes:
# 
#  z = (x bar – μ) / (σ / √n)
#  
# Where:
# X bar = sample mean
# n = sample size
# 
# Relationship to the Standard Normal Distribution:
# 
# The z-statistic follows a standard normal distribution, which has:
# 
# A mean of 0
# A standard deviation of 1
# This distribution is denoted by N(0,1). The z-score essentially re-scales data values from any normal distribution to fit this standard normal distribution. This makes it easier to compare different datasets or assess probabilities using standard tables.
# 
# Z-Statistic in Hypothesis Testing:
# In hypothesis testing, the z-statistic is used to determine how far the observed sample result is from the population parameter under the null hypothesis. The main steps include:
# 
# Formulating hypotheses:
# 
# Null Hypothesis (𝐻0): The population parameter equals a specific value (e.g., μ=μ0).
# Alternative Hypothesis (𝐻1): The parameter differs from that value (two-tailed) or is greater/less than that value (one-tailed).
# 
# Calculating the z-statistic:
# 
# Use the appropriate formula for a z-score to measure how far the sample statistic deviates from the null hypothesis mean.
# 
# Comparing with the critical value:
# 
# For a chosen significance level (𝛼), the critical value(s) from the z-table represent the threshold for rejecting 𝐻0.
# If the calculated z-score falls beyond the critical value(s), the result is considered statistically significant, leading to rejection of the null hypothesis.
# 
# p-value interpretation:
# 
# The p-value is the probability of observing a result as extreme as the sample, assuming the null hypothesis is true. If the p-value is less than 𝛼, 𝐻0 is rejected.
# 
# Example Use Case:
# If we are testing whether a sample mean differs from a population mean (e.g., testing if a new drug's effect differs from the standard treatment), the z-statistic helps quantify the difference. If the z-value is large (far from 0), it indicates that the sample mean is unlikely to have occurred under the null hypothesis.

#  Question2 : What is a p-value, and how is it used in hypothesis testing? What does it mean if the p-value is 
# very small (e.g., 0.01)?

# A p-value is the probability of obtaining a test statistic at least as extreme as the one observed, given that the null hypothesis (𝐻0) is true. It quantifies the evidence against the null hypothesis: the smaller the p-value, the stronger the evidence to reject 𝐻0.
# 
# p-value=P(Observed or more extreme outcome ∣ H0 is true)
# 
# How P-Value is Used in Hypothesis Testing:
# 
# Set a significance level (𝛼):
# Common choices are 0.05 or 0.01. This is the threshold below which the p-value must fall to reject the null hypothesis.
# 
# Compare the p-value with 𝛼:
# 
# If p-value ≤ 𝛼: Reject the null hypothesis (𝐻0). The result is statistically significant.
# If p-value > 𝛼: Fail to reject the null hypothesis. The evidence is insufficient to conclude a significant effect or difference.
# 
# Interpret the p-value:
# 
# A high p-value (close to 1) suggests the observed data is likely under the null hypothesis.
# A low p-value (close to 0) suggests the observed result is unlikely under the null hypothesis, providing stronger evidence against it.
# 
# Meaning of a Very Small P-Value (e.g., 0.01):
# 
# A p-value of 0.01 means there is a 1% probability of obtaining the observed result (or something more extreme) if the null hypothesis is true.
# Interpretation:
# The observed result is unlikely under the null hypothesis.
# With a typical significance level of α=0.05, this p-value would lead to rejection of 𝐻0, as it is smaller than 0.05.

#  Question3: Compare and contrast the binomial and Bernoulli distributions.

# Both the Bernoulli and binomial distributions model discrete outcomes, typically related to success-failure experiments. However, there are key differences between them in terms of scope and application.
# 
# 1. Bernoulli Distribution:
# Definition:
# The Bernoulli distribution describes a random experiment with only two possible outcomes: success (with probability 𝑝) and failure (with probability 1−p).
# 
# Parameters:
# p: Probability of success (where 0≤p≤1)
# 
# Possible Outcomes:
# X=1 (for success)
# X=0 (for failure)
# 
# Probability Mass Function (PMF):
# P(X=x) = p**x(1−p)**1−x,wherex∈{0,1}
# 
# Use Case:
# Models a single trial with a binary outcome (e.g., flipping a coin, where heads = success and tails = failure).
# 
# 2. Binomial Distribution:
# Definition:
# The binomial distribution extends the Bernoulli distribution to the sum of multiple independent Bernoulli trials. It describes the number of successes in a fixed number 𝑛 of independent trials, where each trial has the same probability of success 𝑝.
# 
# Parameters:
# 𝑛: Number of trials
# 𝑝: Probability of success in each trial
# 
# Possible Outcomes:
# The random variable 𝑋 can take values X=0,1,2,…,n, representing the number of successes in 𝑛 trials.
# 
# Probability Mass Function (PMF):
# P(X=k)= (nk) p**k(1-p)**n-k, for k∈{0,1,…,n}
# 
# Where 
# (𝑛𝑘) = n! / k!(n−k)! is the binomial coefficient.
# 
# Use Case:
# Models the total number of successes in multiple independent trials (e.g., counting how many heads occur in 10 coin flips).

# Question 4: Under what conditions is the binomial distribution used, and how does it relate to the Bernoulli 
# distribution?

# Conditions for Using the Binomial Distribution:
# The binomial distribution is appropriate when the following conditions are satisfied:
# 
# Fixed Number of Trials (𝑛):
# There must be a set number 𝑛 of independent trials (or experiments).
# 
# Two Possible Outcomes in Each Trial:
# Each trial must have only two outcomes, often labeled as "success" and "failure".
# Example: Flipping a coin (heads or tails).
# 
# Constant Probability of Success (𝑝):
# The probability of success 𝑝 must remain the same across all trials.
# 
# Example: In a fair coin flip, the probability of heads is always 
# p=0.5.
# 
# Independent Trials:
# The outcome of one trial must not affect the outcomes of others.
# Example: Each coin flip is independent of the previous ones.
# 
# How the Binomial Distribution Relates to the Bernoulli Distribution:
# Single Trial (Bernoulli):
# A Bernoulli distribution describes the outcome of one trial with two possible outcomes: success (1) or failure (0).
# PMF:
# p(X = x) = p**x(1−p)**1−x,wherex∈{0,1}
# 
# Multiple Trials (Binomial):
# The binomial distribution generalizes the Bernoulli distribution to a sequence of 𝑛 independent Bernoulli trials, where the interest is in the total number of successes across the trials.
# PMF:
# 
# P(X=k) = (nk) p**k(1-p)**n-k, for k∈{0,1,…,n}
# 
# Relationship:
# 
# If there is only one trial (n=1), the binomial distribution becomes a Bernoulli distribution.
# Example: 
# X∼Binomial(n=1,p) is the same as X∼Bernoulli(p).
# 
# If you perform multiple independent Bernoulli trials, the sum of their outcomes follows a binomial distribution.
# Example: The total number of heads in 10 coin flips is binomial, as each flip is a Bernoulli trial.

# Question5: What are the key properties of the Poisson distribution, and when is it appropriate to use this 
# distribution?

# The Poisson distribution models the number of times an event occurs within a fixed interval (such as time, area, or volume) when the events happen independently and at a constant average rate. Below are its key properties:
# 
# Discrete Distribution:
# 
# The Poisson distribution is used for count data (e.g., the number of customer arrivals per hour).
# 
# Parameter:
# It has a single parameter 𝜆, which represents the average number of occurrences (or expected value) in the given interval.
# λ>0 (must be positive)
# 
# Probability Mass Function (PMF):
# P(X=k)= (λ**k)(e**-λ) / k!, k=0,1,2,…
# 
# Where:
# 
# 𝑘 is the observed number of events
# 𝑒 is the mathematical constant (approximately 2.718)
# 
# Mean and Variance:
# 
# The mean and variance of the Poisson distribution are both equal to 
# E(X)=λ
# Var(X)=λ
# 
# Memoryless Property:
# 
# Similar to the exponential distribution, the Poisson process is memoryless. The occurrence of events in non-overlapping intervals is independent.
# 
# When to Use the Poisson Distribution:
# The Poisson distribution is appropriate under the following conditions:
# 
# Counting Events in a Fixed Interval:
# 
# You are counting the number of events (e.g., arrivals, defects, requests) within a fixed period, area, or volume.
# Example: Number of calls received by a call center in an hour.
# Events Occur Independently:
# 
# The occurrence of one event does not influence the occurrence of another.
# Example: Customers arriving at a store independently of each other.
# Constant Average Rate:
# 
# The events occur at a constant average rate 
# 𝜆
# λ.
# Example: On average, 5 cars arrive at a toll booth every 10 minutes.
# Low Probability of Multiple Events Simultaneously:
# 
# The probability of more than one event occurring at the exact same time or location is negligible.

#  Question6: Define the terms "probability distribution" and "probability density function" (PDF). How does a 
# PDF differ from a probability mass function (PMF)?

# A probability distribution describes how the probabilities of all possible outcomes of a random variable are distributed. It provides either a probability value for each discrete outcome (in discrete distributions) or a density for continuous outcomes (in continuous distributions).
# 
# For discrete variables: It uses a Probability Mass Function (PMF).
# For continuous variables: It uses a Probability Density Function (PDF).
# 
# Probability Density Function (PDF)
# A PDF describes the likelihood of a continuous random variable taking on a range of values. Unlike probabilities for discrete outcomes, which can be directly measured, the PDF measures density over an interval.
# 
# Key Properties of a PDF:
# f(x)≥0 for all x (the density must be non-negative).
# The total area under the curve of the PDF is equal to 1.
# 
# Difference Between PDF and PMF:
# 
# Type of Random Variable:
# PDF (Probability Density Function): Used for continuous random variables (e.g., height, weight, or time).
# PMF (Probability Mass Function): Used for discrete random variables (e.g., number of heads in coin flips or dice rolls).
# 
# Probability Interpretation:
# PDF: The area under the curve over an interval represents the probability that the variable falls within that interval.
# PMF: The function directly gives the probability of individual outcomes (e.g., 
# P(X=2)).
# 
# Value at a Specific Point:
# PDF: For continuous variables, the probability of a specific value is always 0 (i.e., 
# P(X=x)=0). We only compute probabilities over intervals.
# 
# PMF: For discrete variables, the function gives the exact probability of the variable taking a specific value (e.g., 
# P(X=2)=0.25).
# 
# Total Probability:
# PDF: The integral of the PDF over the entire range of possible values must equal 1.
# PMF: The sum of the probabilities for all possible outcomes must equal 1.
# 
# Examples:
# PDF: Normal distribution, Exponential distribution (e.g., waiting time between events).
# PMF: Binomial distribution, Poisson distribution (e.g., number of events in a fixed interval).

#  Question7: Explain the Central Limit Theorem (CLT) with example.

# The Central Limit Theorem (CLT) is a fundamental concept in statistics that states:
# 
# When independent, identically distributed (i.i.d.) random variables are averaged (or summed), the sampling distribution of the sample mean will approach a normal distribution, regardless of the original distribution of the data, as the sample size 𝑛 becomes large.
# 
# Key Components of CLT:
# Independent and Identically Distributed (i.i.d.) Variables:
# The data points (random variables) must be independent and come from the same distribution.
# 
# Sample Size (n):
# The theorem holds when the sample size 𝑛 is sufficiently large (usually n≥30).
# 
# Mean and Standard Error:
# Mean of the sample mean: 
# E (X bar) = μ (same as the population mean)
# 
# Standard error (SE) of the sample mean:
# 𝜎x bar = 𝜎/underroot n 
# Where 
# 𝜎 is the population standard deviation and 𝑛 is the sample size.
# 
# Normal Approximation:
# As 𝑛 increases, the distribution of sample means approaches a normal distribution with mean μ and standard error 
# 𝜎/underrot n,
# 
# Example of CLT:
# Imagine that a bakery sells cookies, and the weight of each cookie is randomly distributed between 20 grams and 30 grams (uniform distribution). The distribution of cookie weights is not normal.
# 
# Case 1: Single Cookie Weight
# If you randomly pick one cookie, its weight will be somewhere between 20 and 30 grams, with all values equally likely. This distribution is uniform, not normal.
# 
# Case 2: Average Weight of 50 Cookies
# Now, take a random sample of 50 cookies and calculate their average weight.
# 
# If you repeat this process many times (sampling different sets of 50 cookies), the distribution of these sample means will follow a normal distribution, even though the original weight distribution is uniform.
# This happens because of the CLT—the larger the sample size, the closer the sample mean distribution gets to normal, with the mean centered around the population mean.
# 

#  Question8: Compare z-scores and t-scores. When should you use a z-score, and when should a t-score be applied instead?

# Both z-scores and t-scores are used in hypothesis testing and confidence interval estimation to determine how far a sample statistic (like a sample mean) is from the population mean. However, they are applied in different situations, depending on the sample size and whether the population standard deviation is known.
# 
# 1. Z-Score (or Z-Statistic):
# Definition:
# A z-score measures how many standard deviations a data point or sample mean is away from the population mean.
# Formula:
# 
#  z= (X bar - μ)/ (σ/underroot n)
#  
# Where:
# X bar: Sample mean
# 𝜇: Population mean
# σ: Population standard deviation
# n: Sample size
# 
# When to Use Z-Score:
# 
# Population standard deviation (σ) is known.
# Sample size is large (n≥30) because the sample mean will approximately follow a normal distribution (according to the Central Limit Theorem).
# 
# Example:
# If you know the standard deviation of heights in a population, you can use a z-score to determine how far the sample mean height of 50 individuals deviates from the population mean.
# 
# 
# 2. T-Score (or T-Statistic):
# Definition:
# A t-score is used when the population standard deviation (σ) is unknown, and the sample standard deviation (𝑠) is used as an estimate. It accounts for increased uncertainty in small sample sizes.
# Formula:
# t = (X bar −μ) / s/ underroot n
# 
# Where:
# s: Sample standard deviation
# 
# When to Use T-Score:
# 
# Population standard deviation (𝜎) is unknown.
# Sample size is small (n<30).
# When using sample standard deviation (s) to estimate variability.
# 
# Degrees of Freedom (df):
# 
# The t-distribution varies based on degrees of freedom: df=n−1.
# As 𝑛 increases, the t-distribution becomes closer to a standard normal distribution.
# 
# Example:
# If you are studying the effectiveness of a new drug with only 10 participants, you would use a t-score because the sample size is small, and the population standard deviation is not known.
# 

# Question9: Given a sample mean of 105, a population mean of 100, a standard deviation of 15, and a sample 
# size of 25, calculate the z-score and p-value. Based on a significance level of 0.05, do you reject or fail to 
# reject the null hypothesis?
# Task: Write Python code to calculate the z-score and p-value for the given data.
# Objective: Apply the formula for the z-score and interpret the p-value for hypothesis testing.

# Given:
# 
# Sample mean (X bar) = 105
# Population mean (μ) = 100
# Standard deviation (σ) = 15
# Sample size (n) = 25
# Significance level (α) = 0.05
# 
# Step 1: Calculate the Standard Error (SE)
# SE = σ / underroot n
# 
# SE = 15/ underroot 25
# 
# SE = 3
# 
# Step 2: Calculate the Z-Score
# The z-score measures how many standard errors the sample mean is away from the population mean:
# 
# z = (X bar − μ)/SE
# z = 105 - 100/ 3
# z = 1.67
#  
# Step 3: Calculate the P-Value:
# Since this is a two-tailed test, the p-value is computed as:
# p-value=2×(1−CDF(∣z∣))
# Using the cumulative distribution function (CDF) of the standard normal distribution:
# p-value=2×(1−CDF(1.67))≈0.0956 
# 
# Step 4: Compare P-Value with Significance Level (𝛼):
# P-value = 0.0956
# Significance level (α) = 0.05
# Since the p-value (0.0956) is greater than the significance level α=0.05, we fail to reject the null hypothesis.
# 
# Conclusion:
# At a 5% significance level, there is not enough evidence to conclude that the sample mean of 105 is significantly different from the population mean of 100. Thus, we fail to reject the null hypothesis.

# Question10: Simulate a binomial distribution with 10 trials and a probability of success of 0.6 using Python. 
# Generate 1,000 samples and plot the distribution. What is the expected mean and variance?
# Task: Use Python to generate the data, plot the distribution, and calculate the mean and variance.
# Objective: Understand the properties of a binomial distribution and verify them through simulation.

# In[1]:


pip install numpy matplotlib


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


# Parameters for the binomial distribution
n_trials = 10  # Number of trials per sample
p_success = 0.6  # Probability of success in each trial
n_samples = 1000  # Number of samples to generate


# In[4]:


# Generate 1,000 samples from the binomial distribution
samples = np.random.binomial(n=n_trials, p=p_success, size=n_samples)


# In[5]:


# Calculate the sample mean and variance
sample_mean = np.mean(samples)
sample_variance = np.var(samples)


# In[6]:


# Plot the histogram of the binomial distribution
plt.figure(figsize=(10, 6))
plt.hist(samples, bins=range(n_trials + 2), density=True, edgecolor='black', alpha=0.7)
plt.title(f'Binomial Distribution (n={n_trials}, p={p_success}) - 1,000 Samples')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[7]:


# Calculate the theoretical mean and variance
theoretical_mean = n_trials * p_success
theoretical_variance = n_trials * p_success * (1 - p_success)


# In[8]:


# Display the results
print(f'Sample Mean: {sample_mean}')
print(f'Sample Variance: {sample_variance}')
print(f'Theoretical Mean: {theoretical_mean}')
print(f'Theoretical Variance: {theoretical_variance}')


# In[ ]:




