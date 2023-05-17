import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

n = 13385190

#read the result and show it in pandas dataframe with expected value calculated for each query
df2 = pd.read_csv("resultqueries2.txt", sep = " ", header = None, names = ["query", "matches"])
df2['length'] = df2['query'].apply(lambda x: len(x))
df2['expected_matches'] = df2['length'].apply(lambda x: (n-x+1)*(0.25)**x)
df2.to_csv('queries2_output.csv', sep = "\t", index=False)
