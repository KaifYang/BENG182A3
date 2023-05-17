import pandas as pd
n = 13385190
#read the result and show it in pandas dataframe with expected value calculated for each query
df = pd.read_csv("resultqueries.txt", sep = " ", header = None, names = ["query", "matches"])
df['length'] = df['query'].apply(lambda x: len(x))
df['expected_matches'] = df['length'].apply(lambda x: (n-x+1)*(0.25)**x)
df.to_csv('queries_output.csv', sep = "\t", index=False)
