#!/usr/bin/env python

"""
topo_routed.py

Exemplo de topologia Mininet com dois switches e um roteador “LinuxRouter”,
ligando-se a duas interfaces de host criadas externamente (brteste01 e brteste02).

Topo:  Cliente ─ s1 ─ Router ─ s2 ─ Servidor
       (172.18.0.2)  (172.18.0.10/16)   (172.19.0.10/16) (172.19.0.2)

Para usar:
    1) Assegure-se de que as bridges brteste01 e brteste02 já existam.

    2) Execute containers “cliente” e “servidor” nessas redes.

    3) Rode este script como root:

    4) No prompt do Mininet:
       mininet> sh ip route   # para ver as rotas do roteador
       mininet> sh iptables -L  # (opcional) ver se IP forwarding está ativo
       mininet> exit           # sai do Mininet

    5) Dentro de cada container (cliente/servidor), configure a rota padrão
       apontando para o IP do roteador.

    6) Teste a comunicação de ponta a ponta.

Este script usa dois trechos de código de exemplos do Mininet:
- linuxrouter.py  (para criar um host “roteador” com IP forwarding ligado)
- hwintf.py      (para “linkar” uma interface existente do host/contêiner a um switch)

"""

from mininet.net import Mininet
from mininet.node import Node, OVSSwitch
from mininet.link import Link, Intf
from mininet.log import setLogLevel, info
from mininet.cli import CLI
import subprocess

# -------------------------------------------------------
# 1) Classe LinuxRouter: transpõe um host normal para um router
#    copiando ideia do exemplo linuxrouter.py do Mininet.
#    Basta herdar Node, ligar IP forwarding.
# -------------------------------------------------------
class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        # Ativa IP forwarding no kernel
        self.cmd('sysctl net.ipv4.ip_forward=1')

    def terminate(self):
        # Para quando o Mininet for parado
        self.cmd('sysctl net.ipv4.ip_forward=0')
        super(LinuxRouter, self).terminate()


# -------------------------------------------------------
# 2) Função que verifica se a interface (bridge Docker) já existe no host
# -------------------------------------------------------
def checkBridge(bridge_name):
    "Verifica se a interface de bridge existe no sistema"
    result = subprocess.call(['ip', 'link', 'show', bridge_name],
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
    return result == 0


# -------------------------------------------------------
# 3) Topologia principal, criada em um único método para facilitar
# -------------------------------------------------------
def run():
    "Cria rede Mininet com dois switches e um roteador conectado a bridges externas"
    net = Mininet( controller=None, build=False )  # Sem controlador SDN necessário

    info('*** Adicionando o roteador (host Linux com IP forwarding)\n')
    router = net.addHost('r0', cls=LinuxRouter)

    info('*** Adicionando switches\n')
    s1 = net.addSwitch('s1')   # Switch do lado “cliente”
    s2 = net.addSwitch('s2')   # Switch do lado “servidor”

    info('*** Ligando roteador ↔ switches (criando 2 links)\n')
    # Conecta router <--> s1
    net.addLink(s1, router,
                intfName2='r0-eth1',
                params2={'ip': '172.18.0.10/16'})
    # Conecta router <--> s2
    net.addLink(s2, router,
                intfName2='r0-eth2',
                params2={'ip': '172.19.0.10/16'})

    info('*** Construindo a rede\n')
    net.build()

    # ---------------------------------------------------
    # 4) Anexar as bridges Docker (crie-as previamente por fora)
    #    “brteste01” para o switch s1 (lado cliente)
    #    “brteste02” para o switch s2 (lado servidor)
    #    Isso faz com que o container que já esteja conectado a brteste01/02
    #    “veja” minimamente o switch do Mininet.
    # ---------------------------------------------------
    if not checkBridge('veth54c44cd'):
        raise Exception('Bridge brteste01 não encontrada. Crie-a antes (docker network create ...).')
    if not checkBridge('veth1cf7866'):
        raise Exception('Bridge brteste02 não encontrada. Crie-a antes (docker network create ...).')

    info('*** Anexando interface brteste01 ao switch s1\n')
    Intf('brteste01', node=s1)

    info('*** Anexando interface brteste02 ao switch s2\n')
    Intf('brteste02', node=s2)

    info('*** Iniciando o net\n')
    net.start()

    info('\n*** Configurações feitas:\n')
    info('    - Roteador (r0) com interfaces:\n')
    info('        r0-eth0 → 172.18.0.10/16  (lado Cliente)\n')
    info('        r0-eth1 → 172.19.0.10/16  (lado Servidor)\n')
    info('    - Switch s1 conectado a brteste01  (rede 172.18.0.0/16)\n')
    info('    - Switch s2 conectado a brteste02  (rede 172.19.0.0/16)\n')

    info('\n*** No seu container “cliente” (IP 172.18.0.2), adicione:\n')
    info('    ip route add default via 172.18.0.10\n')
    info('\n*** No seu container “servidor” (IP 172.19.0.2), adicione:\n')
    info('    ip route add default via 172.19.0.10\n')

    info('\n*** Agora você pode testar conectividade:\n')
    info('    No cliente: ping 172.19.0.2 (servidor)\n')
    info('    No servidor: ping 172.18.0.2 (cliente)\n\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()