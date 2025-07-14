import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\tmp00258\Desktop\NBA\NBA_player_stats_salaries.csv"

def load_data():
    df = pd.read_csv(FILE_PATH)
    print("\nData loaded successfully!")
    print(df.head())
    return df

def explore_data(df):
    print("\nDataset Information:")
    print(df.info())
    print(f"\nNumber of Players: {df.shape[0]}")
    print(f"Number of Stats/Columns: {df.shape[1]}")
    print(f"\nColumn Names:\n{df.columns.tolist()}")
    print(f"\nUnique Players: {df['Player'].nunique() if 'Player' in df.columns else 'Unknown'}")

def summary_statistics(df):
    columns = ['FG%', '3P%', 'FTA', 'AST', 'STL', 'BLK', 'PTS', 'TRB', 'Salary']
    print("\nSummary Statistics:")
    for col in columns:
        if col in df.columns:
            print(f"\n{col}:")
            print(f"  Mean: {df[col].mean():.2f}")
            print(f"  Median: {df[col].median():.2f}")
            print(f"  Mode: {df[col].mode()[0]:.2f}")
            print(f"  Std Dev: {df[col].std():.2f}")

def visualize_data(df):
    print("\nGenerating combined graphs...")

    fig, axs = plt.subplots(3, 2, figsize=(15, 12))
    fig.suptitle('NBA Player Data Visualizations', fontsize=18)

    # 1. Salary Histogram
    sns.histplot(df['Salary'], color='pink', bins=30, kde=True, ax=axs[0, 0])
    axs[0, 0].set_title('Salary Distribution')
    axs[0, 0].set_xlabel('Salary')
    axs[0, 0].set_ylabel('Number of Players')

    # 2. Scatter: Points vs Salary
    sns.scatterplot(x='PTS', y='Salary', data=df, ax=axs[0, 1])
    axs[0, 1].set_title('Points vs Salary')
    axs[0, 1].set_xlabel('Points per Game')
    axs[0, 1].set_ylabel('Salary')

    # 3. Box Plot: PTS, TRB, AST
    sns.boxplot(data=df[['PTS', 'TRB', 'AST']], ax=axs[1, 0])
    axs[1, 0].set_title('Distribution of Points, Rebounds, Assists')

    # 4. Top 10 Highest Paid Players
    if 'Player' in df.columns:
        top10 = df[['Player', 'Salary']].sort_values(by='Salary', ascending=False).head(10)
        sns.barplot(x='Salary', y='Player', data=top10, palette='viridis', ax=axs[1, 1])
        axs[1, 1].set_title('Top 10 Highest Paid Players')

    # 5. Correlation Heatmap
    corr = df[['FG%', '3P%', 'FTA', 'AST', 'STL', 'BLK', 'PTS', 'TRB', 'Salary']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=axs[2, 0])
    axs[2, 0].set_title('Correlation Heatmap')

    # Empty subplot placeholder
    axs[2, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def answer_questions(df):
    print("\nAnswering Key Questions:")

    # Question 1: Most Well-Rounded (PTS + TRB + AST)
    df['WellRounded'] = df['PTS'] + df['TRB'] + df['AST']
    top_well_rounded = df[['Player', 'WellRounded']].sort_values(by='WellRounded', ascending=False).head(5)
    print("\nTop 5 Well-Rounded Players:")
    print(top_well_rounded.to_string(index=False))

    # Question 2: Best Value Scorers (PTS / Salary)
    df['ValueScore'] = df['PTS'] / df['Salary']
    best_value = df[['Player', 'ValueScore']].sort_values(by='ValueScore', ascending=False).head(5)
    print("\nBest Value Scorers:")
    print(best_value.to_string(index=False))

    # Question 3: Most Efficient Shooters (FG%)
    top_fg = df[['Player', 'FG%']].sort_values(by='FG%', ascending=False).head(5)
    print("\nTop 5 Most Efficient Shooters:")
    print(top_fg.to_string(index=False))

def compare_to_average(df):
    print("\nComparing Players to League Averages:")
    pts_avg = df['PTS'].mean()
    ast_avg = df['AST'].mean()
    trb_avg = df['TRB'].mean()
    print(f"League Averages - PTS: {pts_avg:.2f}, AST: {ast_avg:.2f}, TRB: {trb_avg:.2f}")

    above_avg = df[(df['PTS'] > pts_avg) & (df['AST'] > ast_avg) & (df['TRB'] > trb_avg)]
    print(f"\nPlayers Above Average in PTS, AST, and TRB: {len(above_avg)}")
    print(above_avg[['Player', 'PTS', 'AST', 'TRB']].head(10).to_string(index=False))

def find_most_underpaid(df):
    df['Impact'] = df['PTS'] + df['TRB'] + df['AST']
    df['ValuePerDollar'] = df['Impact'] / df['Salary']
    most_underpaid = df.sort_values(by='ValuePerDollar', ascending=False).iloc[0]
    print("\nMost Underpaid Player Based on Performance:")
    print(f"Player: {most_underpaid['Player']}")
    print(f"Impact Score: {most_underpaid['Impact']:.2f}")
    print(f"Salary: ${most_underpaid['Salary']:.2f}")
    print(f"Value per Dollar: {most_underpaid['ValuePerDollar']:.5f}")

def main():
    print("NBA Player Stats CLI Analysis")
    df = load_data()
    explore_data(df)
    summary_statistics(df)
    visualize_data(df)
    answer_questions(df)
    compare_to_average(df)
    find_most_underpaid(df)

if __name__ == "__main__":
    main()
