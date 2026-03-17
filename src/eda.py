import matplotlib.pyplot as plt

def plot_salary_boxplot(df):
    groups = df.groupby("EducationType")["ConvertedCompYearly"]

    data = [groups.get_group(x) for x in groups.groups]

    plt.boxplot(data, labels=groups.groups.keys())
    plt.title("Salary Distribution by Education Type")
    plt.ylabel("Salary (USD)")
    plt.savefig("outputs/figures/salary_boxplot.png")
    plt.close()