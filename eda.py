import numpy as np
import pandas as pd

def eda(df):
    """Perform exploratory data analysis and save insights to text files."""
    
    # **Insight 1: Descriptive Statistics**
    numeric_df = df.select_dtypes(include=[np.number])
    columns = numeric_df.columns
    
    with open('eda-in-1.txt', 'w') as f:
        f.write("Descriptive Statistics for Numeric Features:\n")
        for col in columns:
            mean_val = numeric_df[col].mean()
            median_val = numeric_df[col].median()
            std_dev = numeric_df[col].std()
            min_val = numeric_df[col].min()
            max_val = numeric_df[col].max()
            range_val = max_val - min_val
            f.write(f'{col}: Mean={mean_val:.2f}, Median={median_val:.2f}, Std Dev={std_dev:.2f}, '
                    f'Min={min_val:.2f}, Max={max_val:.2f}, Range={range_val:.2f}\n')

    # **Insight 2: Correlation Matrix**
    correlation_matrix = numeric_df.corr()
    with open('eda-in-2.txt', 'w') as f:
        f.write("Correlation Matrix Between Features:\n")
        f.write(correlation_matrix.to_string())

    # **Insight 3: Survival Analysis**
    survival_stats = df['Survived'].value_counts(normalize=True) * 100
    with open('eda-in-3.txt', 'w') as f:
        f.write("Survival Analysis:\n")
        f.write(f"Survived: {survival_stats.get(1, 0):.2f}%\n")
        f.write(f"Did Not Survive: {survival_stats.get(0, 0):.2f}%\n")
        if 'Age' in df.columns:
            avg_age_survived = df[df['Survived'] == 1]['Age'].mean()
            avg_age_not_survived = df[df['Survived'] == 0]['Age'].mean()
            f.write(f"Average Age of Survivors: {avg_age_survived:.2f}\n")
            f.write(f"Average Age of Non-Survivors: {avg_age_not_survived:.2f}\n")

    # **Insight 4: Fare Analysis**
    highest_fare = df['Fare'].max()
    lowest_fare = df['Fare'].min()
    avg_fare = df['Fare'].mean()
    fare_range = highest_fare - lowest_fare
    with open('eda-in-4.txt', 'w') as f:
        f.write("Fare Analysis:\n")
        f.write(f"Highest Fare: {highest_fare:.2f}\n")
        f.write(f"Lowest Fare: {lowest_fare:.2f}\n")
        f.write(f"Average Fare: {avg_fare:.2f}\n")
        f.write(f"Fare Range: {fare_range:.2f}\n")
    
    print("EDA completed. Insights saved to eda-in-1.txt, eda-in-2.txt, etc.")

if __name__ == "__main__":
    # Replace with the path to your preprocessed dataset
    df = pd.read_csv("res_dpre.csv")
    eda(df)
