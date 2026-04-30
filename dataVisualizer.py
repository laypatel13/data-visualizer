import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def plot_sales_over_time(df):
    sns.lineplot(x="date", y="sales", data=df)
    plt.xticks(rotation=45)
    plt.title("Sales Over Time")
    plt.tight_layout()
    plt.show()

def plot_sales_by_product(df):
    grouped = df.groupby("product")["sales"].sum().reset_index()
    sns.barplot(x="product", y="sales", data=grouped)
    plt.title("Sales by Product")
    plt.show()

def plot_profit_vs_sales(df):
    sns.scatterplot(x="sales", y="profit", data=df)
    plt.title("Profit vs Sales")
    plt.show()