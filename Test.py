tab = []
N = 20; M = 5
for i in range(N):
    x=[]
    for j in range (M):
        x.append('-')
    tab.append(x)

tab[1][0] = 5
tab[0][1] = 1
print(tab,'','')