import json
import csv

def parse_json_to_csv(file_json, file_csv):
    with open(file_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    header = data[0].keys()

    with open(file_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

    print(f"Arquivo CSV '{file_csv}' gerado com sucesso!")

if __name__ == "__main__":
    parse_json_to_csv("semaforo_dados.json", "semaforo_dados.csv")
