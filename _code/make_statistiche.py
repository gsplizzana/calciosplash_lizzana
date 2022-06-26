import matplotlib.pyplot as plt 
import json

COLORE_SFONDO = 'white'
COLORE_PRIMARIO = "#fb7d07"
with open(f"./_storage/albo_doro/maschile.json", "r") as file:
    data = json.load(file)
file.close()

for doc in data: 
    nominativo = " ".join([x.capitalize() for x in data["NOMINATIVO"].split(" ")])
    nome_file = nominativo.replace(" ","_")
    goals = [int(value) if value != "" else 0 for key,value in doc.items() if key!="GOL" or key!="NOMINATIVO"]
    date  = [key for key in doc.keys() if key!="GOL" or key!="NOMINATIVO"]

    fig,ax = plt.subplots(1,1, dpi=128)
    ax.set_facecolor(COLORE_SFONDO)
    plt.title(f"Statistiche {nominativo}",color=COLORE_PRIMARIO)
    ax.plot(date,goals,color=COLORE_PRIMARIO)

    ax.set_xlim([2004, 2004+len(date)])
    ax.set_xticks(date)
    ax.set_xticklabels(["0"+str(x) if x < 10 else str(x) for x in range(4,23)])
    ax.set_yticks(list(set(goals)))
    ax.tick_params(axis='x', which='minor', labelsize=6)

    plt.tight_layout()
    plt.savefig(f"./assets/statistiche/{nominativo}.png")