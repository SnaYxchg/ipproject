import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
d=pd.read_csv("players.csv")
dt=pd.DataFrame(d)
l1=dt.iloc[:,0]
l2=dt.iloc[:,2]
l3=dt.iloc[:,3]
l4=dt.iloc[:,4]
la=[]
lb=[]
lc=[]
ld=[]
for x in l1:
  la.append(x)
apos=np.arange(len(la))
for x in l2:
  lb.append(x)

for x in l3:
  lc.append(x)

for x in l4:
  ld.append(x)

# plt.bar(apos,lb)
# plt.xticks(apos,la)
# plt.title('BALANCE OF ALL USERS')
# plt.show()

# plt.bar(apos,lc)
# plt.xticks(apos,la)
# plt.title('TOTAL NUMBER OF BETS OF ALL USERS')
# plt.show()

plt.bar(apos,ld)
plt.xticks(apos,la)
plt.title('TOTAL WAGERED OF ALL USERS')
plt.show()