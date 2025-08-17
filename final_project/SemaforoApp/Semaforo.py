import time
import json
import random
import os
from datetime import datetime

class SemaforoIoT:
    def __init__(self, device_id):
        self.device_id = device_id
        self.estados = {
            "VERDE": {"duration": 7, "proximo": "AMARELO"},
            "AMARELO": {"duration": 3, "proximo": "VERMELHO"},
            "VERMELHO": {"duration": 7, "proximo": "VERDE"}
        }
        self.estado_atual = "VERMELHO"
        self.ultima_mudanca = datetime.now().isoformat()

    def mudar_estado(self):
        self.estado_atual = self.estados[self.estado_atual]["proximo"]
        self.ultima_mudanca = datetime.now().isoformat()

    def simular_falha(self):
        return random.random() < 0.05  # 5% chance de falha

    def gerar_dados(self):
        return {
            "device_id": self.device_id,
            "estado": self.estado_atual,
            "timestamp": datetime.now().isoformat(),
            "proxima_mudanca": self.estados[self.estado_atual]["proximo"],
            "falha": self.simular_falha(),
            "bateria": round(random.uniform(20, 100), 2)
        }

def salvar_dados(dados, arquivo="dados/semaforo_dados.json"):
    """Adiciona dados ao arquivo mantendo o histórico"""
    try:
        # Cria diretório se não existir
        os.makedirs(os.path.dirname(arquivo), exist_ok=True)
        
        # Lê dados existentes ou inicia nova lista
        try:
            with open(arquivo, 'r') as f:
                historico = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            historico = []
        
        # Adiciona nova leitura
        historico.append(dados)
        
        # Salva com formatação
        with open(arquivo, 'w') as f:
            json.dump(historico, f, indent=2)
            f.write("\n")  # Quebra de linha no final
            
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def main():
    semaforo = SemaforoIoT("SEMAFORO_001")
    
    try:
        while True:
            # Atualiza estado
            tempo_estado = (datetime.now() - datetime.fromisoformat(semaforo.ultima_mudanca)).seconds
            if tempo_estado >= semaforo.estados[semaforo.estado_atual]["duration"]:
                semaforo.mudar_estado()
            
            # Gera e salva dados
            dados = semaforo.gerar_dados()
            salvar_dados(dados)
            print(f"Dados salvos: {dados['timestamp']}")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nSemaforo desligado")

if __name__ == "__main__":
    main()