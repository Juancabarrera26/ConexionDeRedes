# conexion.py

import os

def configurar_red():
    print("Configurando red con router Movistar Mitrastar GPT-2741GNAC")
    print("SSID: MOVISTAR_FIBRA_C8E8")
    print("Protocolo de seguridad: WPA2-PSK")

def probar_conexion():
    print("Realizando prueba de conexión por cable y WiFi usando Iperf3...")
    
    # Prueba de conexión por cable
    print("Ejecutando prueba por cable...")
    os.system("iperf3 -c 192.168.1.1 -t 10 > resultado_cable.txt")
    
    # Prueba de conexión por WiFi
    print("Ejecutando prueba por WiFi...")
    os.system("iperf3 -c 192.168.1.1 -t 10 > resultado_wifi.txt")

if __name__ == "__main__":
    configurar_red()
    probar_conexion()
