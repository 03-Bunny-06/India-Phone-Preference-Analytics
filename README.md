# India Phone Preference Analysis

## Project Description
This Python script analyzes a dataset (`india_phone_preference.csv`) containing information about mobile phone preferences in India. The script processes the dataset and extracts insights based on gender, brand preference (iPhone vs. Android), payment modes, and purchase platforms.

## Features
- **Handles Missing Data**: Fills missing values with `0`.
- **Gender-based Analysis**:
  - Counts and calculates the percentage of male, female, and other users.
- **Brand Analysis**:
  - Calculates the number and percentage of iPhone and Android users.
  - Analyzes brand preference based on gender.
- **Payment Mode Analysis**:
  - Determines how iPhone and Android users pay (EMI, UPI, Credit Card, Debit Card, or Cash).
- **Purchase Platform Analysis**:
  - Identifies whether users buy online or offline.
  - Breaks down platform preference by gender.

## Dependencies
Ensure you have the following Python libraries installed:

```sh
pip install numpy pandas
```

## Usage
1. Place the `india_phone_preference.csv` file in the same directory as the script.
2. Run the script using:

```sh
python script.py
```

3. The script will output insights into the console in a tabular format.

## Data Format
The `india_phone_preference.csv` dataset should have the following columns:
- `Gender`: Male, Female, Other
- `Brand`: iPhone, Android
- `Payment Mode`: EMI, UPI, Credit Card, Debit Card, Cash
- `Purchase Platform`: Online, Offline

## Output Example
```
--- Gender Meta Data - Male, Females and Others ---
   Male Orders  Female Orders  Others Orders Male Percentage Female Percentage Others Percentage
0       40000         50000          10000        40.00%          50.00%         10.00%

--- Brand Meta Data Iphone or Android ---
   iPhone Orders  Android Orders iPhone Percentage Android Percentage
0         45000         55000         45.00%         55.00%
```
