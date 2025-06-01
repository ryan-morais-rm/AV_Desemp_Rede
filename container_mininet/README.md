# Relatório de configuração

## Explicação

### 1. Redes Virtuais Separadas  
Foram criadas duas redes bridge com sub-redes distintas: uma para o container servidor e outra para o cliente. Essa separação simula dois ambientes isolados, úteis para testes de rede e roteamento.

### 2. Imagem Base Personalizada  
A imagem Docker foi baseada no Ubuntu, contendo ferramentas de rede como ping, ip e iperf. O diretório de trabalho foi definido como /home para organização interna dos containers.

### 3. Execução dos Containers com IPs Fixos  
Os containers foram criados com IPs estáticos e permissão de administração de rede, o que possibilita a adição de rotas personalizadas para comunicação entre as redes.

### 4. Rotas Estáticas para Comunicação  
Como os containers estão em redes distintas, foram adicionadas rotas estáticas em cada um apontando para o IP gateway da outra rede, permitindo o tráfego entre os dois ambientes.

### 5. Mininet  
A configuração do Mininet foi feita para criar uma topologia que simula uma rede com dois switches e um roteador central, conectando dois containers Docker (cliente e servidor) por meio de bridges externas. Utilizamos a API Python do Mininet para definir a topologia. Dois switches foram adicionados (s1 e s2), e o roteador (r0) foi implementado com base na classe LinuxRouter, com suporte a roteamento IP ativado. O switch s1 foi conectado a uma interface de bridge (brteste01) já existente no host, que por sua vez estava ligada ao container cliente. O mesmo foi feito para o switch s2, conectado à bridge brteste02, associada ao container servidor.

Durante a configuração, enfrentamos dificuldades para conectar as bridges Docker (brteste01 e brteste02) diretamente no Mininet usando o script hwintf.py. O problema ocorreu porque o Mininet, por padrão, espera interfaces de rede físicas ou reconhecidas pelo sistema (como eth0, br0), e as bridges do Docker não são vistas da mesma forma. O hwintf.py busca por interfaces reais, mas as bridges Docker não aparecem como tais.

Para resolver, identificamos as interfaces virtuais (vethXXXX) que estão ligadas às bridges Docker. Essas interfaces, criadas automaticamente pelo Docker, são as que de fato conectam os containers às bridges. Ao utilizar os nomes dessas interfaces no hwintf.py em vez do nome da bridge (brteste01 ou brteste02), conseguimos integrar corretamente o ambiente Docker à topologia do Mininet.

---

