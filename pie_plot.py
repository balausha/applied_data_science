import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def trophies_by_team(matches):
    """
    This function is used to count total matches won by each IPL team from
    the dataset.
    Parameter : matches ( It is a dataframe )
    """
    matches_won = matches.groupby('winner').count()['id'].reset_index()
    return matches_won

matches=pd.read_csv("C:/Users/Lenovo/Downloads/New folder (3)/matches.csv")
matches_won=trophies_by_team(matches)

labels = ['CSK' ,'DC', 'DCap', 'DD' ,'GL', 'KXI', 'KTK' ,'KKR' ,'MI',
          'PW', 'RR' ,'RPS', 'RPSs', 'RCB', 'SH']

plt.figure(figsize=(10, 12))
plt.pie(matches_won['id'], autopct="%0.001f%%", labels=labels, startangle=90,  radius=0.98)
plt.title('Matches won by each IPL team')

# Move the legend outside the figure
plt.legend(loc='center left', bbox_to_anchor=(1.005, 0.75))
plt.show()
