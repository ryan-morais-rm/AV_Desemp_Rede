import os
import re

# Diretório onde estão os arquivos de texto
diretorio = "./"  # ou o caminho correto, ex: "./resultados"

perdas_C = []
perdas_D = []

# Função para extrair o percentual de perda de um arquivo
def extrair_perda_arquivo(path):
    with open(path, 'r') as f:
        for linha in f:
            if "packet loss" in linha:
                match = re.search(r"(\d+\.?\d*)% packet loss", linha)
                if match:
                    return float(match.group(1))
    return None  # caso não encontre

# Loop sobre os 51 experimentos
for i in range(1, 51):
    arquivo_C = os.path.join(diretorio, f"exp-{i:03d}-B-C.txt")
    arquivo_D = os.path.join(diretorio, f"exp-{i:03d}-B-D.txt")
    
    perda_C = extrair_perda_arquivo(arquivo_C)
    perda_D = extrair_perda_arquivo(arquivo_D)
    
    perdas_C.append(perda_C if perda_C is not None else 0.0)
    perdas_D.append(perda_D if perda_D is not None else 0.0)

print("Perdas C:", perdas_C)
print("Perdas D:", perdas_D)
