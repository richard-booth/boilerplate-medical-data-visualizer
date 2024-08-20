import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = df['weight'] / ((df['height'] /100) ** 2 )
df['overweight'] = np.where( df['weight'] / ((df['height'] /100) ** 2 ) > 25, 1, 0)


# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)




# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df,
        id_vars=['cardio'],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    # 6
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))



    

    # 7
    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar", order=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])



    # 8
    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar", order=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]).fig



    # 9
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

    # 10
def draw_heat_map():
    # Clean the data
    df_heat = df[ (df['weight'] <= df['weight'].quantile(0.975))  #5 weight is more than the 97.5th percentile
            & (df['weight'] >= df['weight'].quantile(0.025)) #4 weight is less than the 2.5th percentile
            & (df['height'] <= df['height'].quantile(0.975)) #3 height is more than the 97.5th percentile
            & (df['height'] >= df['height'].quantile(0.025)) #2 height is less than the 2.5th percentile
            & (df['ap_lo'] <= df['ap_hi'])] #1 diastolic pressure is higher than systolic ap_lo > ap_hi

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr))

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    heatmap_fig = sns.heatmap(corr, annot=True, square=True, center=0, annot_kws={'fontsize':7 }, linewidths=0.5, mask=mask, fmt='.1f')
    fig = heatmap_fig.figure

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

