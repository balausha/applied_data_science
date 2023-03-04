matches=matches[matches['season'] >= 2016]
matches_won=trophies_by_team(matches)
matches_won

def trophies_by_team(matches):
    """
    This function is used to count total matches won by each IPL team from
    the dataset.
    Parameter : matches ( It is a dataframe )
    """
    matches_won = matches.groupby('winner').count()['id'].reset_index()
    return matches_won
    
plt.scatter(matches_won['winner'], matches_won['id'], color="orange")
plt.xlabel('Team')
plt.ylabel('Matches Won')
plt.title("Total number of Matches won by each IPL team")
plt.xticks(rotation = 90)
plt.show()
