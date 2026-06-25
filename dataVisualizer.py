import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from colorama import init, Fore, Back, Style

init(autoreset=True)

sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#f8f9fa", "figure.facecolor": "#f8f9fa"})


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"Loaded {file_path} successfully!" + Style.RESET_ALL)
        return df
    except Exception as e:
        print(Fore.WHITE + Back.RED + f"Fatal Error: Failed to load file. {e}" + Style.RESET_ALL)
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
    print("\n" + Fore.BLACK + Back.WHITE + "--- Data Visualizer ---" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + "(1) Sales Over Time" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + "(2) Sales By Product" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + "(3) Profit vs Sales" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.NORMAL + "(4) Quit" + Style.RESET_ALL)

def main():
    file_path = input(Fore.CYAN + Style.BRIGHT + "Enter CSV file path: " + Style.RESET_ALL)
    df = load_data(file_path)
    if df is None:
        return

    while True:
        show_menu()
        choice = input("\n" + Fore.CYAN + Style.BRIGHT + "Enter Your Choice: " + Style.RESET_ALL)

        if choice == "1":
            plot_sales_over_time(df)
        elif choice == "2":
            plot_sales_by_product(df)
        elif choice == "3":
            plot_profit_vs_sales(df)
        elif choice == "4":
            print(Fore.WHITE + Style.BRIGHT + "Bye! Thanks For Using Data Visualizer!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid Choice, Try Again!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()