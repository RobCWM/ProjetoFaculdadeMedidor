# Importando bibliotecas
import time
import random

# Função para simular leitura de temperatura
def ler_temperatura():
    return random.uniform(18.0, 30.0)  # Simula temperatura entre 18 e 30 graus Celsius

# Função para enviar alerta
def enviar_alerta(temp):
    print(f"ALERTA: Temperatura alta detectada: {temp:.2f}°C")

# Função principal
def monitorar_temperatura(limite_superior):
    print("Iniciando monitoramento de temperatura...")
    while True:
        temperatura = ler_temperatura()
        print(f"Temperatura atual: {temperatura:.2f}°C")
        if temperatura > limite_superior:
            enviar_alerta(temperatura)
        time.sleep(5)  # Espera 5 segundos antes da próxima leitura

# Configurando o limite de temperatura
limite = 25.0  # Temperatura limite para alerta

# Iniciando o monitoramento
monitorar_temperatura(limite)