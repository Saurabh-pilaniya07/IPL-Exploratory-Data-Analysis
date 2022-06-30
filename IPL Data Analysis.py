
#IPL Data Analysis

#EDA on IPL Dataset

# Commented out IPython magic to ensure Python compatibility.
#importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

#importing IPL matches DataSet
data = pd.read_csv("/content/matches.csv")

data.head(10)

# Rows & Columns
data.shape

data.info

# Names of All the Columns
data.columns

# Data Pre-processing: Finding out NaN values
data.isna().any()

# Statistical Description of Dataset
data.describe()

# No. of Matches played
data['id'].count()

# Citys where Matches are Played.
data['Season'].unique()

# Team Won by scoring the Maxmimum Runs
data.iloc[data['win_by_runs'].idxmax()]

# Team Won by Consuming the Maxmimum Wickets
data.iloc[data['win_by_wickets'].idxmax()]

# Which season consisted of the highest number of matches ever played
fig_dims = (20, 4)
fig, ax = plt.subplots(figsize=fig_dims)
sns.countplot(x = 'Season', ax=ax, data=data)
plt.show()

# Most Successful IPL Team
data1 = data.winner.value_counts()
sns.barplot(y = data1.index, x = data1)

# The Probability of Winning a Match if the Toss was Won
probability_of_win = data['toss_winner'] == data['winner']
probability_of_win.groupby(probability_of_win).size()

sns.countplot(probability_of_win)

plt.hist(data.win_by_runs)
plt.grid(True)
plt.show()

data.plot(x='toss_winner',y='win_by_runs')
plt.show()

# Higher Row Width
pd.set_option('max_rows', 99999)
pd.set_option('max_colwidth', 400)
pd.describe_option('max_colwidth')

# Highest wins by Teams Per sesson
data.groupby('Season')['winner'].value_counts()

data['toss_decision'].value_counts()

# Man of the match
data['player_of_match'].value_counts()

# City were the number of matches Played
data['city'].value_counts()

