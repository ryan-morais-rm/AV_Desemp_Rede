import os
import re
import csv

# Caminho da pasta com os logs
log_dir = '/home/ryan-correia/Área de trabalho/projetos/repositorios/github/AV_Desemp_Rede/container_mininet2/resultados/clientes/5ms/udp/'

# Regex para qualquer linha de dados (tanto TCP quanto UDP)
# Pega: intervalo, throughput numérico, unidade (Gbits/sec ou Mbits/sec)
pattern_generic = re.compile(r"\[\s*\d+\]\s+([\d\.]+-[\d\.]+)\s+sec\s+[\d\.]+\s+(G|M)Bytes\s+([\d\.]+)\s+(G|M)bits/sec")

# Cria pasta para CSVs
csv_dir = os.path.join(log_dir, 'csv')
os.makedirs(csv_dir, exist_ok=True)

# Processa cada log
for fname in os.listdir(log_dir):
    if fname.startswith('log') and fname.endswith('.txt'):
        full_path = os.path.join(log_dir, fname)
        with open(full_path, 'r') as f:
            lines = f.readlines()

        csv_name = fname.replace('.txt', '_dados.csv')
        csv_path = os.path.join(csv_dir, csv_name)

        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Intervalo (seg)', 'Throughput (Mbits/sec)'])

            for line in lines:
                match = pattern_generic.search(line)
                if match:
                    intervalo = match.group(1)
                    throughput_val = float(match.group(3))
                    throughput_unit = match.group(4)

                    # Se for Gbits/sec → converte pra Mbits/sec
                    if throughput_unit == 'G':
                        throughput_mbps = throughput_val * 1000
                    else:
                        throughput_mbps = throughput_val

                    writer.writerow([intervalo, throughput_mbps])

print(f"\n✅ Parser genérico concluído! CSVs gerados em: {csv_dir}\n")

