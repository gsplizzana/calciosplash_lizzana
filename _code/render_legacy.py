import json
import datetime as dt
from tqdm import tqdm

def make_dettagli(anno, index, document):
    dettagli = ["---", "layout: post", f"date: {document['data']}", "categories: partite", f"permalink: /torneo/{anno}/{index}", "---"]
    dettagli.append(f'**Girone**: {document["gironi"]}\n')
    dettagli.append(f'Data: {document["data"]}\n')
    dettagli.append(f'| | {document["squadra_1"].rstrip()} | {document["squadra_2"].rstrip()} |')
    dettagli.append("|:-----:|-----|-----|")
    dettagli.append("|".join(["Risultato", str(document["gol_squadra_1"]), str(document["gol_squadra_2"])]))
    dettagli.append("|".join(["Goals", "<br/>".join([f"{'⚽' * d} {k}" for k, d in eval(document["goleador_1"]).items()]),
                              "<br/>".join([f"{'⚽' * d} {k}<br/>" for k, d in eval(document["goleador_2"]).items()])]))
    dettagli.append("|".join(["Autogoals", "<br/>".join([f"{'⛔' * d} {k}" for k, d in eval(document["autogol1"]).items()]),
                              "<br/>".join([f"{'⛔' * d} {k}<br/>" for k, d in eval(document["autogol2"]).items()])]))
    dettagli.append("|".join(["Falli", str(document["falli_squadra_1"]) if "falli_squadra_1" in document else "",
                              str(document["falli_squadra_2"]) if "falli_squadra_2" in document else ""]))
    dettagli.append("|".join(["Gialli", "<br/>".join(document["gialli1"]), "<br/>".join(document["gialli2"])]))
    dettagli.append("|".join(["Rossi", "<br/>".join(document["rossi1"]), "<br/>".join(document["rossi2"])]))
    dettagli.append("|".join(["Miglior Giocatore", "<br/>".join([f"{'⭐' * d} {k}<br/>" for k, d in document["best_giocatore_1"].items()]),
                              "<br/>".join([f"{'⭐' * d} {k}<br/>" for k, d in document["best_giocatore_2"].items()])]))
    dettagli.append("|".join(["Miglior Portiere", "<br/>".join([f"{'⭐' * d} {k}<br/>" for k, d in document["best_portiere_1"].items()]),
                              "<br/>".join([f"{'⭐' * d} {k}<br/>" for k, d in document["best_portiere_2"].items()])]))
    dettagli = "\n".join(dettagli)
    with open(f"./../partite/{anno}-{index}.markdown", "w", encoding="utf-8") as file:
        file.write(dettagli)

def render_calciosplash(anno):
    path = f"./../_legacy/calciosplash_{anno}/torneo_{anno}.json"
    with open(path, "r") as file:
        data = json.load(file)

    markdown = ["\n".join(["---", "layout: post", f"date: {dt.datetime.now()}", "categories: torneo", f"permalink: /torneo/{anno}/", "---"])]
    markdown.append("| PARTITA | GIRONE | DATA|  INCONTRO | RISULTATO | GENERE |DETTAGLI |")
    markdown.append("|:-----:|-----|-----|-------|------|----|------|")

    for index, document in tqdm(data[f"torneo_{anno}"].items(), desc=f"Rendering torneo {anno}"):
        try:
            link = f"[Info](/calciosplash_lizzana/torneo/{anno}/{index})"
            genere = "🍻" if document["genere_gironi"] == 1 else "🍸"
            row = [index, document["gironi"], f"{document['data']}", f'{document["squadra_1"].rstrip()} - {document["squadra_2"].rstrip()}',
                   f'{document["gol_squadra_1"]} - {document["gol_squadra_2"]}', genere, link]
            markdown.append("| ".join([str(x) for x in row]))
            #if anno == 2019 or anno == 2018:
            make_dettagli(anno,index,document)
        except Exception as e:
            print(e)

    results = "\n".join(markdown)
    with open(f"./../tornei/{anno}.markdown", "w", encoding="utf-8") as file:
        file.write(results)


if __name__ == "__main__":
    for anno in [2019, 2018, 2017, 2016, 2015, 2014]:
        render_calciosplash(anno=anno)
