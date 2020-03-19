import pandas as pd
import numpy as np

ipl_auction =pd.read_csv("Match.csv")
type(ipl_auction)
pd.set_option("display.max_columns", 8)
ipl_auction.head(5)
list(ipl_auction.columns)
ipl_auction.head(5).transpose()
ipl_auction.shape
ipl_auction.info()
ipl_auction[:5]
ipl_auction[-5:]
ipl_auction["ManOfMach"][:5]
ipl_auction[["ManOfMach", 'Team1']][:5]
ipl_auction.iloc[1:9, 1:8]
ipl_auction.Win_Margin.value_counts()
ipl_auction.Win_Margin.value_counts(normalize=True)*100
pd.crosstab(ipl_auction['Team1'], ipl_auction["Toss_Winner"])
pd.crosstab(ipl_auction['Team1'], ipl_auction["match_winner"])
ipl_auction[['Team1','Team2', 'match_winner']].sort_values('match_winner")

