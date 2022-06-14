import json
from datetime import datetime as dt

def clean_entry(entry):
    cleaned = {}
    for key,value in entry.items():
        cleaned_key = key.replace("\n"," ").strip()
        cleaned_value = value.replace("\n"," ").strip()
        cleaned.update({cleaned_key:cleaned_value})
    return cleaned

def load_template():
    with open("./_storage/template_gironi.markdown", "r") as file:
        template = file.read()
    file.close()
    return template

def make_classifica(classifica):
    table = []
    table.append("|**pos**|**Squadra**|**Pt.**|**GF**|**GS**|**DR**|")
    table.append("|:-----:|-----------|-------|------|------|------|")
    for n,entry in enumerate(classifica):
        entry = clean_entry(entry)
        table.append(f"{n}| {entry['Squadra'].strip()} | {entry['P'].strip()} | {entry['F'].strip()} | {entry['S'].strip()} | {entry['DR'].strip()} |")

    table.append("{:class='styled-table'}")
    return "\n".join(table)

def make_risultati(risultati):
    table = ["\n"]
    
    for entry in risultati:
        entry = clean_entry(entry)
        table.append(f"{entry['Team1'].strip()} | {entry['Goal1'].strip()} | - | {entry['Goal2'].strip()} | {entry['Team2'].strip()} |")
    table.append("{:class='styled-table'}")
    return "\n".join(table)

def create_gironi(data):
    gironi = ""
    for key in data.keys():
        if type(data[key]) != dict:
             continue
        gironi += f"<h3>Girone {key}</h3>\n"
        gironi += "----\n\n"
        gironi += make_risultati(data[key]["RISULTATI"]) if "RISULTATI" in data[key] else ""
        gironi += "\n\n"
        gironi += make_classifica(data[key]["CLASSIFICA"]) if "CLASSIFICA" in data[key] else ""
        gironi += "\n\n"
    return gironi

def fill_template(data,template):
    template = template.replace("DATA_TORNEO",f"{dt.now()}")
    template = template.replace("URL_TORNEO",f"/tornei/{data['TORNEO']}/{data['GENERE']}")
    gironi = create_gironi(data)
    template = template.replace("GIRONI", gironi)
    return template

if __name__ == "__main__":
    docs = ["femminili_2014",
            "femminili_2015",
            "femminili_2016",
            "femminili_2017",
            "femminili_2019",
            "maschili_2014",
            "maschili_2015",
            "maschili_2016",
            "maschili_2017",
            "maschili_2018",]

    for doc in docs:
        print(f"Rendering {doc}")
        with open(f"./_storage/{doc}.json", "r") as file:
            data = json.load(file)
        file.close()
        template = load_template()
        template = fill_template(data, template)
        with open(f"./tornei/{doc}.markdown", encoding="Latin-1", mode="w") as file:
            file.write(template)
        file.close()