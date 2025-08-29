# Iris Dataset Analysis

This project performs an exploratory data analysis (EDA) on the famous Iris flower dataset using Python and popular data science libraries.

## Overview

The Iris dataset is a classic multivariate dataset introduced by Ronald Fisher in 1936. It contains measurements of 150 iris flowers from three different species (setosa, versicolor, and virginica), with 50 samples from each species.

## Features

The dataset includes the following four features for each sample:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

## Requirements

To run this code, you need the following Python libraries:

- pandas
- matplotlib
- seaborn
- scikit-learn

You can install these dependencies using pip:
```
pip install pandas matplotlib seaborn scikit-learn
```

## Code Structure

The code is organized into four main sections:

1. **Data Loading and Exploration**
   - Loads the Iris dataset from scikit-learn
   - Creates a pandas DataFrame with the feature data and species labels
   - Displays the first few rows of the dataset
   - Checks dataset information and missing values

2. **Basic Data Analysis**
   - Computes descriptive statistics for the dataset
   - Calculates mean values grouped by species

3. **Data Visualization**
   - Creates four different visualizations:
     - Line chart showing cumulative sepal length by species
     - Bar chart displaying average petal length per species
     - Histogram of sepal length distribution
     - Scatter plot of sepal length vs. petal length colored by species

4. **Key Findings**
   - Prints summary insights about the dataset and relationships between features

## Usage

1. Ensure you have all the required libraries installed
2. Run the script in a Python environment
3. The script will:
   - Load and explore the dataset
   - Perform basic analysis
   - Generate visualizations (which will be displayed in separate windows)
   - Print key findings to the console

## Key Findings

Based on the analysis:
1. Petal measurements differ more strongly between species than sepal measurements
2. Setosa species has distinctly smaller petal length/width compared to Versicolor and Virginica
3. Sepal length distribution is fairly normal, with slight variation between species
4. Scatter plot shows that petal length can clearly separate species groups

## Visualizations

The code generates the following visualizations:
1. Line Chart: Cumulative Sepal Length by Species
2. Bar Chart: Average Petal Length per Species
3. Histogram: Distribution of Sepal Length
4. Scatter Plot: Sepal Length vs. Petal Length (colored by species)

These visualizations help in understanding the relationships between different features and how they vary across species.
