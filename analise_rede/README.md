# Avaliação de Desempenho de Rede: Atraso e Perda de Pacotes

**Autor:** Ryan de Morais Correia  
**Data:** 30 de Maio de 2025

## 🔍 Introdução
Este experimento teve como objetivo analisar o desempenho de rede em termos de **atraso (latência)** e **perda de pacotes**, utilizando o comando `ping` entre dois nós de origem (A e B) e dois destinos (C e D).

---

## ⚙️ Ambiente de Testes

- **Origem A**: IP `10.0.0.12`
- **Origem B**: IP `192.168.15.14`
- **Destino C**: `www.fifa.com` (ex: `23.219.67.9`)
- **Destino D**: `www.gmail.com` (ex: `142.250.219.133`)

- Foram realizados **50 experimentos para cada par de origem-destino**, com 30 pacotes ICMP por experimento, totalizando 100 experimentos no total.

---

## 📈 Resultados e Gráficos

### Série Temporal de Atraso (Exemplo B → C)

- A série mostra **variação abrupta** no tempo de resposta.
- Explicação: distância do roteador Wi-Fi ao laptop B influenciando negativamente a estabilidade da rede.

---

### Média de Atraso por Experimento

#### B → C e B → D
- Alta **flutuação** nos valores de atraso.
- Intervalos de confiança amplos.
- Evidência de **instabilidade na rede**, sugerindo variações de rota, congestionamento ou interferência.

#### A → C e A → D
- Atraso **baixo e estável**.
- Intervalos de confiança estreitos.
- Desempenho **confiável e consistente**.

---

### Perda de Pacotes por Experimento

#### A → C e A → D
- Praticamente **nenhuma perda** registrada.
- Apenas **1 perda isolada** no destino C.
- Indica um **ambiente de rede bem configurado e estável**.

#### B → C e B → D
- **Ocorrência frequente de perdas**, com variação entre 1% e valores mais altos.
- Comportamento **instável e inconsistente**.
- Possíveis causas:
  - Limitações no nó B (hardware ou localização)
  - Interferência local
  - Variações na qualidade dos enlaces de rede

---

## 🧾 Conclusão

- O nó **A apresentou melhor desempenho geral**: baixa latência, mínima perda de pacotes, e comportamento estável.
- O nó **B apresentou flutuações acentuadas**, com perdas recorrentes e maior variabilidade nos atrasos.
- Caminhos iniciados em **A são preferíveis para aplicações críticas**, devido à sua **confiabilidade e consistência**.

