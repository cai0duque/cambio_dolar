import requests
import openpyxl
from openpyxl import Workbook
from datetime import datetime
import schedule
import time

EXCEL_FILE = "cotacao_dolar.xlsx"

# Buscar a cotação do Dólar
def buscar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cotacao = float(data["USDBRL"]["bid"])
        return cotacao
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

# Atualizar o Excel
def atualizar_excel():
    cotacao = buscar_cotacao()
    if cotacao is None:
        print("Não foi possível obter a cotação.")
        return

    # Verificar se o arquivo Excel já existe
    try:
        workbook = openpyxl.load_workbook(EXCEL_FILE)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Data", "Hora", "Cotação (USD/BRL)"])

    # Adicionar os dados
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    sheet.append([data, hora, cotacao])

    # Salvar em EXCEL
    workbook.save(EXCEL_FILE)
    print(f"Arquivo Excel atualizado: {data} {hora} - R$ {cotacao:.2f}")

# Função para agendar a execução
def agendar_atualizacoes():
    schedule.every(1).hour.do(atualizar_excel)  # Atualizar a cada 1 hora
    print("Agendamento iniciado. Atualizando a cada 1 hora.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print("Iniciando o bot de câmbio Dólar/BRL...")
    atualizar_excel()
    agendar_atualizacoes()
