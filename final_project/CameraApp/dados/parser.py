import json
import csv

def parse_ndjson(input_file, output_file):
    registros = []
    buffer = ""

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buffer += line
            if line.endswith("}"):  # fim de um objeto JSON
                try:
                    obj = json.loads(buffer)
                    registros.append(obj)
                except json.JSONDecodeError as e:
                    print("Erro ao parsear:", e)
                buffer = ""

    # Salva em CSV
    if registros:
        keys = registros[0].keys()
        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(registros)

    print(f"Convertido {len(registros)} registros para {output_file}")


if __name__ == "__main__":
    parse_ndjson("dados/camera_dados.json", "dados/camera_dados.csv")
