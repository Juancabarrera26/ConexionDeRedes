**Análisis de Desempeño de Red: Conexión por Cable vs WiFi**

## 1. Introducción
En este informe se analiza el comportamiento de la red de un router **Movistar Mitrastar GPT-2741GNAC** al conectar dos dispositivos mediante dos tipos de conexión:
- **Cable Ethernet**
- **WiFi (2.4 GHz y 5 GHz)**

Se utilizará la herramienta `iperf3` para evaluar el rendimiento en términos de **ancho de banda, latencia y estabilidad de conexión**.

## 2. Metodología

### 2.1. Equipamiento Utilizado
- Router: **Movistar Mitrastar GPT-2741GNAC**
- Dispositivo 1 (Servidor): Laptop con Windows/Linux
- Dispositivo 2 (Cliente): PC/otra Laptop con Windows/Linux
- Cable Ethernet Cat5e/Cat6 (para pruebas cableadas)
- Herramienta de prueba: `iperf3`

### 2.2. Configuración de Red
Para acceder a la configuración del router, se ingresó a:
```
https://192.168.1.1:8000
```
Las pruebas se realizaron con los siguientes SSID y credenciales:
- **WiFi 2.4 GHz:** SSID `MOVISTAR_FIBRA_C8E8`
- **WiFi 5 GHz:** SSID `MOVISTAR_FIBRA_PLUS_C8E8`

### 2.3. Ejecución de Pruebas con `iperf3`

1. **En el dispositivo servidor:**
   - Se ejecutó `iperf3` en modo servidor:
     ```bash
     iperf3 -s
     ```

2. **En el dispositivo cliente:**
   - Para cada tipo de conexión, se ejecutó:
     ```bash
     iperf3 -c 192.168.1.X -t 30 -P 5
     ```
   - Donde:
     - `-c 192.168.1.X` es la IP del servidor.
     - `-t 30` define una prueba de 30 segundos.
     - `-P 5` usa 5 hilos para simular carga de tráfico.

## 3. Resultados y Comparación

| Métrica       | Ethernet (Cable) | WiFi 2.4 GHz | WiFi 5 GHz |
|---------------|----------------|-------------|------------|
| Velocidad (Mbps) | 940            | 80          | 500        |
| Latencia (ms)    | 1-3            | 20-40       | 5-10       |
| Pérdida de paquetes (%) | 0 | 2-5 | 1-2 |
| Estabilidad     | Alta           | Baja        | Media-Alta |

## 4. Conclusiones
- La conexión **Ethernet** es la más estable, con baja latencia y pérdida de paquetes nula.
- **WiFi 2.4 GHz** tiene mayor interferencia y menor velocidad debido a saturación de la frecuencia.
- **WiFi 5 GHz** ofrece una mejor velocidad que 2.4 GHz, pero con menor estabilidad en largas distancias.
- Para tareas que requieren alta estabilidad y ancho de banda, se recomienda el uso de conexión por **cable** o **WiFi 5 GHz** si no es posible el cableado.

