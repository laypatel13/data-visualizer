# Data Visualizer

A command-line tool that loads and visualizes CSV data using charts. Helps users quickly understand trends, comparisons, and relationships in their data.

## Motivation
Raw data is hard to interpret without visuals. This tool makes it easy to turn CSV data into meaningful charts for quick insights.

## Features
Load and explore CSV data
Visualize sales over time (line chart)
Compare sales by product (bar chart)
Analyze profit vs sales (scatter plot)
Interactive menu-based interface
Supports any properly formatted CSV file

## Project Structure
data-visualizer/
├── visualizer.py       # main application
├── data/
│   └── sample.csv      # sample dataset
├── requirements.txt    # project dependencies
└── README.md           # project documentation

## How to Run
git clone https://github.com/laypatel13/data-visualizer.git
cd data-visualizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 visualizer.py

## Example Output
--- Data Visualizer ---

Enter CSV file path: data/sample.csv

1. Sales over time
2. Sales by product
3. Profit vs Sales
4. Exit

Select an option (1-4): 1

(Line chart window opens showing sales trend)

## What I Learned
Working with Pandas for data loading and manipulation
Creating visualizations using Seaborn and Matplotlib
Structuring Python code using functions
Building interactive CLI tools
Handling user input and errors

## Built With
Python 3
Pandas
Seaborn
Matplotlib