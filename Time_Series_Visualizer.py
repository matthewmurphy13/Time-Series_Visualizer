import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates= True, index_col= 'date')

#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset
#or bottom 2.5% of the dataset.
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
def draw_line_plot():
    #Draw Line Plot
    fig, ax = plt.subplots(figsize= (12,4))
    ax = sns.lineplot(data= df, x= 'date', y= 'value')
    plt.xlabel = 'Date'
    plt.ylabal = 'Site Views'
    plt.title = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'
    #Save Figure
    fig.savefig('line_plot.png')
    return fig
print(draw_line_plot())

#Draw Bar Plot
df_bar = df.copy()
df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
df_bar['year'] = pd.DatetimeIndex(df_bar.index).year

#It should show average daily page views for each month grouped by year.
df_bar = df_bar.groupby(['year','month'])['value'].mean()
df_bar = df_bar.unstack()
df_bar.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept','Oct', 'Nov', 'Dec']

def draw_bar_plot():
    fig = df_bar.plot(kind='bar', figsize=(15, 10)).figure
    plt.title = 'Bar Graph'
    plt.xlabel = 'Years'
    plt.ylabel = 'Average Per Views'
    plt.legend(loc='upper left', title='Months')
    return fig

print(draw_bar_plot())

#Create a Box Plot
df_box = df.copy().reset_index()
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

def draw_box_plot():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    sns.boxplot(ax=ax1, x='year', y='value', data=df_box)
    ax1.set_title('Year-wise Box Plot')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(ax=ax2, x='month', y='value', data=df_box)
    ax2.set_title('Month-wise Box Plot')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    return fig

print(draw_box_plot())
