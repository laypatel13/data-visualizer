# 📉 Data Visualizer - CLI
A simple command-line Data Visualizer built using Python. This project helps you visualize CSV data through interactive charts with a colorful CLI interface powered by Matplotlib and Seaborn.

---

## ✨ Features

- Visualize sales trends over time with a line chart
- Compare total sales by product with a bar chart
- Analyze profit vs sales correlation with a scatter plot
- Colorful CLI output for better readability

---

## 📦 Install via pip

```bash
pip install laypatel13-data-visualizer
```

Then run it from anywhere in your terminal:

```bash
data-visualizer
```

---

## 🛠️ Install from source

```bash
git clone https://github.com/laypatel13/data-visualizer.git
cd data-visualizer
pip install -r requirements.txt
pip install -e .
```

Then run:

```bash
data-visualizer
```

---

## 📂 Project Structure

```text
data-visualizer/
├── data_visualizer/
│   ├── __init__.py
│   └── main.py
├── sample-data.csv
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧰 Built With

- Used [Pandas](https://pandas.pydata.org/) for data loading and processing.
- Used [Matplotlib](https://matplotlib.org/) for chart rendering.
- Used [Seaborn](https://seaborn.pydata.org/) for styled visualizations.
- Used [Colorama](https://pypi.org/project/colorama/) for colored terminal output.