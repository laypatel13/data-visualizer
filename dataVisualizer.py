import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Enhance global look and feel
sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#f8f9fa", "figure.facecolor": "#f8f9fa"})


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def plot_sales_over_time(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="date", y="sales", data=df, marker="o", linewidth=2.5, markersize=8, color="#1f77b4")
    plt.xticks(rotation=45)
    plt.title("Sales Over Time", fontsize=16, fontweight='bold', pad=15)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Sales", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_sales_by_product(df):
    plt.figure(figsize=(8, 6))
    grouped = df.groupby("product")["sales"].sum().reset_index()
    grouped = grouped.sort_values(by="sales", ascending=False)
    ax = sns.barplot(x="product", y="sales", data=grouped, hue="product", palette="viridis", legend=False)
    plt.title("Total Sales by Product", fontsize=16, fontweight='bold', pad=15)
    plt.xlabel("Product", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontsize=11)
    plt.tight_layout()
    plt.show()

def plot_profit_vs_sales(df):
    plt.figure(figsize=(9, 6))
    sns.scatterplot(x="sales", y="profit", data=df, hue="product", palette="Set2", s=100, edgecolor='w', alpha=0.8)
    plt.title("Profit vs Sales", fontsize=16, fontweight='bold', pad=15)
    plt.xlabel("Sales", fontsize=12)
    plt.ylabel("Profit", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title="Product", title_fontsize='11', fontsize='10')
    plt.tight_layout()
    plt.show()

def show_menu():
    print("\n----Data Visualizer----")
    print("1.Sales over time")
    print("2.Sales by product")
    print("3.Profit vs Sales")
    print("4.Exit")


def main():
    file_path = input("Enter CSV file path: ")

    df = load_data(file_path)

    if df is None:
        return

    while True:
        show_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            plot_sales_over_time(df)
        elif choice == "2":
            plot_sales_by_product(df)
        elif choice == "3":
            plot_profit_vs_sales(df)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1-4.")


main()