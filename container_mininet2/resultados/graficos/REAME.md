# 📡 Projeto de Avaliação de Desempenho de Redes com Mininet e iPerf

## 👤 Autor

**Ryan de Morais Correia**  
Curso: Redes de Computadores – IFPB  
Repositório: [GitHub - ryan-morais-rm](https://github.com/ryan-morais-rm)

---

## 📌 Objetivo

Avaliar o desempenho de diferentes cenários de rede variando parâmetros como largura de banda, atraso, taxa de perda, protocolo de transporte (TCP/UDP) e número de clientes. O objetivo é compreender o impacto desses fatores sobre o throughput durante a simulação de tráfego em um ambiente virtualizado com Mininet e Docker.

---

## ⚙️ Planejamento Experimental

Foram definidos 5 parâmetros principais para os testes:

| Parâmetro               | Valores Testados           |
|-------------------------|----------------------------|
| **Largura de Banda (bw)**  | 100 Mbps, 200 Mbps         |
| **Atraso (delay)**         | 1 ms, 5 ms                 |
| **Perda (loss)**           | 1%, 5%                     |
| **Protocolo de Transporte**| TCP, UDP                   |
| **Número de Clientes**     | 1, 2                       |

Total de **32 cenários**. Cada experimento durou **120 segundos**.

---

## 🧰 Ferramentas Utilizadas

- **Mininet** com suporte a Docker containers.
- **iPerf (v2)** como gerador e analisador de tráfego.
- **Shell Script e Python** para automação e análise dos resultados.
- **Matplotlib** para visualização dos dados.

---

## 🚀 Metodologia

1. Criação automatizada dos 32 cenários variando os parâmetros.
2. Execução do iPerf em modo cliente-servidor:
   ```bash
   iperf -c <ip_servidor> -t 120 -i 1      # Para TCP
   iperf -c <ip_servidor> -u -t 120 -i 1   # Para UDP

