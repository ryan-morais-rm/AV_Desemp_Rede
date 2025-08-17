import time
import random
import json
from datetime import datetime

class CameraIoT:
    def __init__(self, device_id, resolution=(640, 480)):
        self.device_id = device_id
        self.resolution = resolution  # largura x altura
        self.online = True

    def capture_frame(self):
        """Simula captura de um frame (pixels falsos)."""
        width, height = self.resolution
        avg_brightness = random.randint(0, 255)

        frame_data = {
            "device_id": self.device_id,
            "timestamp": datetime.utcnow().isoformat(),
            "resolution": f"{width}x{height}",
            "avg_brightness": avg_brightness,
            "motion_detected": random.choice([True, False]),
        }
        return frame_data
    

    def stream(self, duration=10, interval=2, output_file=None):
        """Simula envio de frames por um tempo determinado."""
        resultados = []
        start = time.time()
        while time.time() - start < duration:
            frame = self.capture_frame()

            print(json.dumps(frame, indent=2))

            if output_file:
                with open(output_file, "a") as f:
                    f.write(json.dumps(frame, indent=2) + "\n")

            time.sleep(interval)


if __name__ == "__main__":
    try:
        camera = CameraIoT("CAMERA_001", resolution=(1280, 720))
        camera.stream(duration=20, interval=2, output_file="dados/camera_dados.json")

    except KeyboardInterrupt:
        print("Câmera Interrompida")
