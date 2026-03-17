from scipy.stats import f_oneway
import numpy as np

def anova_test(df):
    groups = df.groupby("EducationType")["ConvertedCompYearly"]
    samples = [group for _, group in groups]

    f_stat, p_value = f_oneway(*samples)
    return f_stat, p_value


def cohens_d(group1, group2):
    diff = group1.mean() - group2.mean()
    pooled_std = np.sqrt((group1.std()**2 + group2.std()**2) / 2)
    return diff / pooled_std