import pandas as pd

n = 10**7
m = 10**7
r = 100
Llist = [5, 11, 15, 20, 25, 30, 35, 40]

df = pd.DataFrame(Llist, columns=["l"])

df["Speedup"] = (n*m)/(n+m+r*m*(r-df["l"]+1)*(n-df["l"]+1)*((1/4)**df["l"]))

df["Sensitivity"] = 1-(1-(0.85)**df["l"])**((m/r)*(r-df["l"]+1)) 

# Speedup = [(n*m)/(n+m+r*m*(r-l+1)*(n-l+1)*((1/4)**l)) for l in Llist]

# Sensitivity = [1-(1-(0.85)**l)**((m/r)*(r-l+1)) for l in Llist]

# with open("q2.txt", "w") as f:
#     for i in range(len(Llist)):
#         f.write(str(Llist[i]) + " " + str(Speedup[i]) + " " + str(Sensitivity[i]) + "\n")

print(df)