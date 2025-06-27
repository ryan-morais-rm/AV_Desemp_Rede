import pandas as pd
import matplotlib.pyplot as plt
import os

# Dados com mais de 1 cliente
# Pasta com os CSVs de conexão TCP
# Possui dados com 1ms
csv_dir = '/home/ryan-correia/Área de trabalho/projetos/repositorios/github/AV_Desemp_Rede/container_mininet2/resultados/clientes/1ms/tcp/csv'

csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

for file in csv_files:
    path = os.path.join(csv_dir, file)
    df = pd.read_csv(path)

    plt.plot(df['Intervalo (seg)'], df['Throughput (Mbits/sec)'], label=file.replace('_dados.csv',''))

plt.xticks(rotation=90)
plt.xlabel('Tempo')
plt.ylabel('Throughput (Mbits/sec)')
plt.title('Evolução do Throughput por Cenário')
plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.grid(True)
plt.show()

