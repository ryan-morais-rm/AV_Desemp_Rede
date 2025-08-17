import json
import csv

arquivo_json = "leituras.json" 
arquivo_csv = "leituras.csv"

with open(arquivo_json, "r", encoding="utf-8") as fin, open(arquivo_csv, "w", newline="", encoding="utf-8") as fout:
    fieldnames = ["timestamp", "temperatura", "co2", "o2"]
    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for linha in fin:
        registro = json.loads(linha.strip())
        writer.writerow(registro)

print(f"✅ Conversão concluída! Arquivo salvo como {arquivo_csv}")