# NBA Player Stats CLI Analysis

This Python program performs exploratory data analysis and visualization on NBA player statistics and salary data. It helps uncover trends, identify underpaid or overperforming players, and visualize relationships between performance metrics and salary.

## Features

- Load and explore NBA player stats from a CSV file
- Summary statistics for key metrics (FG%, PTS, AST, TRB, Salary, etc.)
- Combined multi-graph visualization:
  - Salary histogram
  - Scatter plot: Points vs Salary
  - Box plot: Points, Rebounds, Assists
  - Bar chart: Top 10 highest paid players
  - Heatmap: Correlation matrix
- Identifies:
  - Most well-rounded players
  - Best value scorers (high performance, low salary)
  - Most efficient shooters
  - Most underpaid player overall
- Compares players to league averages across key stats

## Visualization Preview

- Histogram: Salary distribution
- Scatter Plot: Points per Game vs Salary
- Box Plot: PTS, TRB, AST comparisons
- Bar Chart: Top 10 Salaries
- Heatmap: Correlation between key stats

## Usage

1. Place your NBA CSV dataset at:
   C:\Users\tmp00258\Desktop\NBA\NBA_player_stats_salaries.csv

2. Save the Python script as main.py in the same folder.

3. Open Command Prompt or PowerShell and run:
   cd C:\Users\tmp00258\Desktop\NBA
   python main.py

   If python doesn’t work, try:
   py main.py

## Requirements

- Python 3.8 or newer
- Required libraries:
  pip install pandas numpy matplotlib seaborn

## Dataset Assumptions

The CSV file should include the following columns (at minimum):

- Player – player name
- FG%, 3P%, FTA, AST, STL, BLK, PTS, TRB, Salary – performance and salary data

## What You'll Learn

- Basic Python data analysis with pandas and numpy
- Visualization with matplotlib and seaborn
- Summary statistics (mean, median, mode, standard deviation)
- Correlation analysis
- Real-world insight generation from sports data

## Example Questions Answered

- Who are the top 5 most well-rounded players?
- Which players give the best scoring value per dollar?
- Who are the most efficient shooters in the league?
- Who is the most underpaid high performer?
- How do your favorite players compare to league averages?
