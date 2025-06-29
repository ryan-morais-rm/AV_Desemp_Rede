import os
import re
import csv

# Caminho da pasta com os logs UDP
log_dir = '/home/ryan-correia/Área de trabalho/projetos/repositorios/github/AV_Desemp_Rede/container_mininet2/resultados/cliente/1ms/udp'

# Regex para capturar linhas do tipo: [  1] 0.0000-1.0000 sec   131 KBytes  1.07 Mbits/sec
pattern_udp = re.compile(
    r'\[\s*\d+\]\s+(\d+\.\d+)-(\d+\.\d+)\s+sec\s+([\d\.]+)\s+KBytes\s+([\d\.]+)\s+Mbits/sec')

# Cria pasta para os CSVs se não existir
csv_dir = os.path.join(log_dir, 'csv')
os.makedirs(csv_dir, exist_ok=True)

# Processa todos os arquivos de log UDP
for fname in os.listdir(log_dir):
    if fname.endswith('.txt') and fname.startswith('log_'):
        full_path = os.path.join(log_dir, fname)
        with open(full_path, 'r') as f:
            lines = f.readlines()

        csv_name = fname.replace('.txt', '_dados.csv')
        csv_path = os.path.join(csv_dir, csv_name)

        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Início (s)', 'Fim (s)', 'Transferência (KBytes)', 'Throughput (Mbits/sec)'])

            for line in lines:
                match = pattern_udp.search(line)
                if match:
                    inicio = float(match.group(1))
                    fim = float(match.group(2))
                    transferencia = float(match.group(3))
                    throughput = float(match.group(4))
                    writer.writerow([inicio, fim, transferencia, throughput])

print(f"\n✅ Parser UDP concluído! CSVs gerados em: {csv_dir}\n")

