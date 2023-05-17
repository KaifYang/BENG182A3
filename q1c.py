string = "AATAAGCCGC"

prob = {"A":0.1, "T":0.1, "C":0.4, "G":0.4}

totalprob = 0

for i in range(len(string)-4):
    substring = string[i:i+5]   
    subprob = 1

    for j in range(5):
        subprob *= prob[substring[j]]
    
    totalprob += subprob

print(str(totalprob) + "(n-4)")
