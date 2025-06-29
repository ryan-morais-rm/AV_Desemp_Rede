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
3. Salvamento da saída do cliente em arquivos .txt.
4. Parser dos logs para formato .csv com script Python.
5. Geração de gráficos com base nos dados de throughput ao longo do tempo.

## GRÁFICOS
1. O gráfico image_notebook1.py tem informações de:
   Clientes único, conexão TCP e 1ms. 
2. O gráfico image_notebook2.py tem informações de:
   Clientes único, conexão UDP e 1ms. 
3. O gráfico image_notebook3.py tem informações de:
   Clientes único, conexão TCP e 5ms.
4. O gráfico image_notebook4.py tem informações de:
   Clientes único, conexão UDP e 5ms. 
5. O gráfico image_notebook1.py tem informações de:
   Clientes dependentes, conexão TCP e 1ms. 
6. O gráfico image_notebook2.py tem informações de:
   Clientes dependentes, conexão UDP e 1ms. 
7. O gráfico image_notebook3.py tem informações de:
   Clientes dependentes, conexão TCP e 5ms.
8. O gráfico image_notebook4.py tem informações de:
   Clientes dependentes, conexão UDP e 5ms.

## RESULTADOS
-> TCP - 1ms - Clientes

Os logs TCP indicam que a rede oferece alta capacidade e desempenho robusto para transferência de dados pesados. O protocolo TCP regula automaticamente a taxa de envio para evitar congestionamento, o que causa oscilações naturais no throughput. O cliente 1 teve um desempenho ligeiramente superior e mais estável que o cliente 2, mas ambos alcançaram transferências significativas, acima de 250 GB em 2 minutos, com médias entre 18 e 21 Gbps.

-> TCP - 5ms - Clientes

Apesar do delay de 5 ms, a largura de banda sustentada é muito alta, o que mostra que a rede tem uma boa capacidade e a latência ainda está dentro de limites toleráveis para conexões de alta taxa. O throughput fica consistentemente entre 24.5 e 25.6 Gbits/sec em mais da metade do tempo (principalmente do segundo 30 ao 80), indicando alta estabilidade com pequenos outliers.

-> UDP - 5ms - Cliente único

Durante a análise dos experimentos, foi observado um padrão recorrente nos arquivos log11_cliente.txt, log15_cliente.txt, log3_cliente.txt e log7_cliente.txt. Esses logs apresentaram saídas muito semelhantes entre si, especialmente no que diz respeito aos valores de jitter e RTT. Em todos eles, o jitter se manteve relativamente estável, com pequenas variações ao longo do tempo, enquanto os valores de RTT apresentaram oscilações pontuais, porém dentro de uma faixa considerada aceitável para os testes realizados. Essa similaridade sugere que os cenários configurados nesses casos tiveram comportamento de rede bastante próximo, possivelmente devido a condições de tráfego, topologia ou parâmetros de envio semelhantes.

-> UDP - 5ms - Clientes

Os arquivos log_12client1.txt, log_12client2.txt, log_16client1.txt, log_16client2.txt, log_4client1.txt, log_4client2.txt, log_8client1.txt e log_8client2.txt apresentaram um desempenho um pouco melhor em comparação com outros experimentos, especialmente em termos de estabilidade do jitter e tempos de resposta (RTT) ligeiramente mais baixos. Ainda assim, o comportamento geral entre eles foi bastante semelhante: os padrões de variação do jitter foram discretos e os valores de RTT oscilaram dentro de limites considerados aceitáveis. Esse desempenho consistente e levemente superior pode estar relacionado a fatores como menor contenção de rede, otimização de parâmetros de envio ou melhor distribuição de tráfego durante os testes. Esses logs indicam cenários em que a comunicação UDP se manteve estável, com desempenho acima da média, porém sem mudanças bruscas no comportamento dinâmico da rede.

## CONCLUSÃO
![image](https://github.com/user-attachments/assets/d1b35376-2f84-444b-81ef-2ed155faf539)

