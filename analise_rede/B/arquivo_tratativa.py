import os
import re
import csv

# Diretório onde estão os arquivos .txt
entrada_dir = "/home/ryan-correia/Área de trabalho/ifpb/AVD/pratica_1/B"

# Diretório onde os CSVs tratados serão salvos
saida_dir = os.path.join(entrada_dir, "dados_tratados")
os.makedirs(saida_dir, exist_ok=True)

# Expressões regulares
tempo_re = re.compile(r'time=([\d.]+) ms')
perda_re = re.compile(r'(\d+)% packet loss')

# Processa todos os arquivos .txt que começam com 'exp-' e terminam com '.txt'
for nome_arquivo in os.listdir(entrada_dir):
    if nome_arquivo.startswith("exp-") and nome_arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(entrada_dir, nome_arquivo)
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()

        tempos = []
        perda = None

        for linha in linhas:
            tempo_match = tempo_re.search(linha)
            if tempo_match:
                tempos.append(float(tempo_match.group(1)))
            perda_match = perda_re.search(linha)
            if perda_match:
                perda = int(perda_match.group(1))

        # Nome do CSV
        nome_csv = nome_arquivo.replace(".txt", ".csv")
        caminho_csv = os.path.join(saida_dir, nome_csv)

        # Escreve o CSV
        with open(caminho_csv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Ping nº', 'Tempo (ms)'])
            for i, t in enumerate(tempos, 1):
                writer.writerow([i, t])
            writer.writerow([])
            writer.writerow(['Perda de Pacotes (%)', perda])

saida_dir  # Retorna o caminho onde os arquivos foram salvos
