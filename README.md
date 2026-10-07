# Data Gathering, Cleaning, and Preprocessing

## Overview

This repository contains a complete Python-based data cleaning and preprocessing pipeline created for the Junior Data Scientist Internship task. Raw real-world datasets often contain missing values, inconsistent formats, invalid data types, and extreme outliers. This project provides a robust methodology for identifying and resolving these issues to prepare raw data for downstream Exploratory Data Analysis (EDA) and predictive modeling.

## Key Features & Preprocessing Steps

1. **Data Exploration & Standardization**: Standardized column names to lowercase format and inspected initial dataset structure.


2. **Type Coercion**: Converted non-standard date formats and string values into valid `datetime` and `float64` data types.


3. **Missing Value Imputation**: Replaced missing numerical values with column medians and imputed missing date values using forward filling (`ffill`).


4. **Outlier Capping**: Applied the Interquartile Range (IQR) method and statistical thresholding to cap extreme outliers without losing data points.


5. **Categorical Encoding**: Converted binary categorical variables into numerical format.


6. **Feature Scaling**: Scaled continuous numerical features using Min-Max Normalization to bring values into a standard range [0, 1].

## File Structure

```text
├── DataGatheringCleaningandPreprocessing.py   # Main Python script for data processing[cite: 3, 4]
├── cleaned_dataset.csv                       # Exported clean dataset[cite: 1, 4]
└── README.md                                 # Project documentation

## Prerequisites

Ensure you have Python installed along with the required libraries:

```bash
pip install pandas numpy

## How to Run

1. **Clone the repository**:
```bash
git clone https://github.com/aryaevuru14/Data-Gathering-Cleaning-and-Preprocessing.git
cd Data-Gathering-Cleaning-and-Preprocessing

```


2. **Run the Python script**:
```bash
python DataGatheringCleaningandPreprocessing.py

```


3. **Output**:
The script will display the initial raw dataset alongside the processed results in the terminal and generate `cleaned_dataset.csv` in the root folder.
