AV DESEMP REDE  Análise em Atraso e Perda

Ryan de Morais Correia
30 de Maio de 2025


Introdução
Explicação geral
Apresentação dos resultados
Conclusão

Explicação geral
Descrição dos experimentos: O objetivo deste experimento é medir o tempo de resposta (atraso) e o percentual de perda de pacotes em comunicações de rede utilizando o comando ping, entre dois nós origem (denominados A e B) e dois destinos (C e D). A rigor, esses testes buscam analisar o comportamento da rede em diferentes trajetos, observando o desempenho em termos de latência e confiabilidade de entrega
Ambiente de testes: Os testes foram realizados em uma rede local, por meio de conexões à internet a partir dos nós A (“10.0.0.12”) e B(“192.168.15.14”) com conectividade estável. Os experimentos foram organizados com base nos seguintes nós:
A e B: Hosts a partir do qual todos os testes foram iniciados.                                 
C: Host (www.fifa.com) como primeiro destino de parte dos testes (ex:23.219.67.9). 
D: Host (www.gmail.com) como segundo destino de parte dos testes (ex:142.250.219.133). 
Procedimento experimental: Para cada destinatário, foram realizados 50 experimentos distintos, totalizando 100 experimentos no total. Cada experimento consistiu na execução do comando “ping” com 30 envios consecutivos, utilizando-se do exemplo:
> ping -c ${SAMPLESIZE} ${SITE_C} > exp-${EXP}-${SOURCE}-C.txt 
Métricas observadas: As métricas extraídas de cada experimento foram o tempo de resposta individual, em milissegundos (ms), para cada um dos 30 pacotes ICMP enviados, indicado por “time=XX.X ms” na saída do ping. A rigor, pela perda de pacotes, sendo seus percentuais não recebidos, indicados por uma linha semelhante a 0% packet loss ao final da execução do ping. 


Apresentação dos resultados
Série Temporal de Atraso de um Único Experimento
A figura a seguir apresenta uma série temporal de atraso observada durante a execução de um único experimento de comunicação entre o host B e o host C. O arquivo utilizado foi o exp-005-B-C.txt, contendo os tempos de resposta de 30 pacotes ICMP consecutivos enviados a partir do host B para o host C. 
Neste gráfico: 
- > O eixo horizontal representa a sequência das amostras, numeradas de 1 a 30, correspondendo a cada pacote enviado. 
-> O eixo vertical apresenta o tempo de resposta (RTT) de cada pacote, medido em milissegundos (ms). 
A variação nos tempos observados reflete uma variação abrupta da latência de rede, influenciada por fatores como congestionamento, qualidade do enlace, e possíveis variações de rota. A rigor, nesse caso específico, a variação ocorre devido a distância que o roteador wi-fi estava do laptop B, por isso existe essa instabilidade da comunicação no caminho de rede. 

Figura 1 - Série temporal dos tempos de resposta (em ms) para o experimento 005 entre os hosts A e D. Cada ponto representa o tempo de resposta de um dos 30 pacotes ICMP enviados. 
Série Temporal da Média de Atraso por Experimento (B -> C e B-> D)

Figura 2 - Série temporal das médias de atraso para 50 experimentos a partir de B para os destinos C e D. As barras verticais representam o intervalo de confiança de 95% para cada média observada. Unidade: milissegundos (ms).
A  série temporal apresentada na figura 2 demonstra uma instabilidade significativa nos valores médios de atraso, o que é reforçado pelos seguintes pontos:
-> A presença de flutuações acentuadas ao longo dos experimentos, com picos e vales irregulares, sugere variação dinâmica da rede. O desvio padrão elevado confirma estatisticamente essa instabilidade. O intervalo entre o valor mínimo e o valor máximo é considerável, o que evidencia comportamentos extremos ao longo da série. Esses comportamentos podem estar associados a fatores como congestionamento intermitente na rede, alterações no caminho de roteamento, problemas transitórios no host de destino ou nos enlaces intermediários. 





Série Temporal da Média de Atraso por Experimento (A -> C e A-> D)

Figura 3 – Série temporal das médias de atraso para 50 experimentos a partir de A para os destinos C e D. As barras verticais representam o intervalo de confiança de 95% para cada média observada. Unidade: milissegundos (ms).
A Figura 3 apresenta a série temporal das médias de atraso (em milissegundos) observadas para cada um dos 50 experimentos realizados a partir do host A em direção aos hosts C e D. Para cada experimento, foram coletadas 30 amostras de tempo de resposta (RTT), a partir das quais foi calculada a média e o intervalo de confiança (IC) com 95% de confiança
-> O eixo horizontal mostra a sequência dos 50 experimentos (de 1 a 50, sem unidade).
-> O eixo vertical apresenta o tempo médio de resposta em milissegundos (ms). 
Cada curva representa um destino “A -> C” em azul e “A -> D” em laranja. As barras verticais indicam o intervalo de confiança de 95% para cada média. 




Percentual de Perda de Pacotes por Experimento (A -> C, A -> D).

Figura 4 - reforça a conclusão de que, do ponto de vista da confiabilidade da entrega de pacotes, ambos os caminhos A -> C e A -> D operaram com alto grau de sucesso, apresentando virtualmente nenhuma perda de dados durante os testes.
De forma geral, observa-se um comportamento extremamente estável e confiável da rede, com nenhuma perda de pacotes registrada em 49 dos 50 experimentos, tanto para C quanto para D. A única exceção identificada foi uma perda isolada no destino C, onde uma barra surge no gráfico, indicando que ao menos um dos 30 pacotes enviados não chegou ao destino. Esse comportamento pode ser interpretado como indício de um ambiente de rede bem configurado, sem congestionamentos ou falhas de roteamento frequentes. A única perda observada pode estar relacionada a:
-> Uma anomalia momentânea, como ruído na conexão ou instabilidade breve na rota.
-> Um evento de transbordamento de buffer em algum roteador ou switch no caminho para o host C.
-> Alguma atividade paralela no ambiente de teste (processos em execução, limitação de recursos da máquina, etc.).
Mesmo com essa exceção, o percentual de perda global é negligenciável e estatisticamente insignificante, sendo um forte indicativo da qualidade do canal de comunicação entre os nós.


Considerações:
-> O fato de não haver perdas no host D em nenhum dos experimentos reforça a robustez da conexão A → D em termos de entrega de pacotes.
-> A estabilidade do gráfico, com a predominância de barras zeradas, facilita a análise visual e destaca ainda mais o comportamento atípico do experimento em que ocorreu perda para o destino C.

Percentual de Perda de Pacotes por Experimento (B -> C, B-> D). 


O Gráfico 5 apresenta o percentual de pacotes perdidos em cada um dos 50 experimentos realizados a partir do nó B para os destinos C e D. Neste caso, cada experimento também é representado por um par de barras verticais — uma para o destino C e outra para o destino D — indicando, em termos percentuais, o número de pacotes que foram enviados, mas não chegaram ao destino. Diferentemente do que foi observado na comunicação A -> C/D (Gráfico 4), neste cenário os resultados evidenciam um comportamento instável e flutuações significativas no desempenho da rede. Diversas barras não nulas se destacam tanto para o destino C quanto para o destino D, indicando a ocorrência frequente de perdas de pacotes durante os experimentos.



Observações principais:
> A presença de múltiplos pontos com perdas superiores a 0% demonstra uma instabilidade mais recorrente no canal B → C e B → D.
> A variação do percentual de perda entre os experimentos é ampla, com alguns experimentos apresentando perdas leves (1 a 3%) e outros valores mais elevados, indicando possíveis momentos de congestionamento ou falha de roteamento.                    > Em alguns experimentos, o destino C apresentou maior percentual de perda que o destino D, enquanto em outros a situação se inverte — sugerindo que as flutuações não estão restritas a um único caminho, mas ocorrem de forma dinâmica nos dois fluxos de rede.
Possíveis causas:
> O nó B pode estar localizado em uma posição de rede com maior latência média, maior número de saltos, ou recursos de hardware mais limitados (CPU/RAM), o que pode influenciar negativamente a estabilidade.                                                                       > Interferência ou sobrecarga de tráfego local no host B durante os testes pode ter gerado perdas intermitentes.                                                                                                     > Os caminhos entre B → C e B → D podem estar sujeitos a variações na qualidade do enlace físico ou virtual, dependendo da topologia e roteamento da rede em uso.
Comparações estatísticas:
> A média de perdas nos experimentos B → C e B → D é substancialmente mais alta do que nos experimentos A → C e A → D (Gráfico 4), reforçando a diferença de confiabilidade entre os nós de origem.
> O desvio padrão das perdas também é consideravelmente maior, indicando uma variabilidade expressiva entre os experimentos.




Conclusão
Durante este experimento, realizamos a análise de desempenho da rede com base em medições de atraso e perda de pacotes entre os nós A e B em direção aos destinos C e D. Foram gerados gráficos de séries temporais, médias com intervalos de confiança e gráficos de barras com perdas percentuais para ilustrar os resultados. A partir dos gráficos, observou-se que o nó A apresentou desempenho mais estável e confiável em ambas as métricas: os atrasos de A → C e A → D foram baixos e com pouca variabilidade, e as perdas de pacotes foram praticamente inexistentes. Em contrapartida, o nó B demonstrou instabilidade, com maior flutuação no atraso e ocorrência frequente de perdas de pacotes tanto para C quanto para D. Portanto, o caminho iniciado em A foi superior em todos os aspectos, mostrando-se mais adequado para transmissões críticas e sensíveis a atraso ou perda
