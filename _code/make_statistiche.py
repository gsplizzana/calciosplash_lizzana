import matplotlib.pyplot as plt 

goals = [0] * 11 + [4,1,4,4,9] + [0,0,0]
date  = [int("200"+str(x)) if x < 10 else int("20"+str(x)) for x in range(4,23,1) ]

fig,ax = plt.subplots(1,1, dpi=128)
ax.set_facecolor('white')
plt.title("Statistiche Raffelli Davide",color="#fb7d07")
ax.plot(date,goals,color="#fb7d07")
ax.set_xlim([2004, 2022])
ax.set_xticks(date)
ax.set_xticklabels(["0"+str(x) if x < 10 else str(x) for x in range(4,23)])
ax.set_yticks(list(set(goals)))
ax.tick_params(axis='x', which='minor', labelsize=6)

plt.tight_layout()
plt.savefig("./assets/statistiche/raffaelli_davide.png")