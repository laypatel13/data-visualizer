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