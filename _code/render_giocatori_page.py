import os

markdown = []
header = "\n".join(["---", "layout: page", "title: Giocatori", "permalink: /gspedia/giocatori", "---"])
markdown.append(header)
markdown.append("\n")
markdown.append("# Giocatori")
markdown.append("\n")
markdown.append("---")
markdown.append("\n")
row = ""
pagine_giocatori = os.listdir("./../giocatori")
pagine_giocatori.sort()
for n, giocatori in enumerate(pagine_giocatori):
    giocatori = giocatori.replace(".markdown","")
    giocatore = " ".join([x.capitalize() for x in giocatori.split("_")])
    row += " | " + f"[{giocatore}](giocatori/{giocatori})"
    if n % 3 == 0:
        row = row + " |"
        markdown.append(row)
        row = ""

if markdown[-1].endswith("|") == False:
    markdown[-1]+=" |"

markdown = "\n".join(markdown)

with open(f"./../giocatori.markdown", "w", encoding="utf-8") as file:
    file.write(markdown)