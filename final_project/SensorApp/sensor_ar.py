import json
import random
import time
from datetime import datetime

def simular_dados():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperatura": round(random.uniform(18, 30), 1),
        "co2": random.randint(300, 2000),
        "o2": random.randint(300, 2000),
    }

if __name__ == "__main__":
    try:
        while True:
            dados = simular_dados()
            with open("/sensordados/leituras.json", "a") as f:
                f.write(json.dumps(dados) + "\n")
            time.sleep(5)
    except KeyboardInterrupt: 
        print("Sensor encerrado")