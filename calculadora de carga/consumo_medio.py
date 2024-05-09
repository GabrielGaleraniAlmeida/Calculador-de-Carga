import requests
import pandas as pd
import logging
import time

# Configurar o log para registrar informações e erros em um arquivo de log
logging.basicConfig(filename='log.txt', level=logging.INFO)

def obter_dados_da_api(ano, estacao):
    """
    Esta função recupera dados da API para um ano e temporada específicos.
    São necessários dois argumentos: ano (int) e estacao (str).
    Ele retorna a resposta da API no formato JSON se for bem-sucedido ou Nenhum se houver um erro.
    """
    url = f"https://dados.ons.org.br/api/v1/dataset/carga-energia-verificada/data?year={ano}&season={estacao}"
    try:
        resposta = requests.get(url)
        logging.info(f"Requesting {url}: {resposta.status_code}")
        if resposta.status_code!= 200:
            logging.error(f"Failed to request {url}: {resposta.text}")
            return None
        return resposta.json()
    except requests.RequestException as e:
        logging.error(f"Error requesting {url}: {e}")
        return None

def calcular_consumo_medio(ano, estacao):
    """
    Esta função calcula o consumo médio para um ano e estação específicos.
    São necessários dois argumentos: ano (int) e estacao (str).
    Retorna o consumo médio se for bem-sucedido ou Nenhum se houver erro.
    """
    dados = obter_dados_da_api(ano, estacao)
    if dados is None:
        logging.error(f"Failed to get data for {ano} {estacao}")
        return None
    consumo = [item['carga_global'] for item in dados]
    consumo_medio = sum(consumo) / len(consumo)
    logging.info(f"Consumo médio for {ano} {estacao}: {consumo_medio:.2f}")
    return consumo_medio

def process_year_season(ano, estacao):
    """
    Esta função processa um único ano e estação.
    São necessários dois argumentos: ano (int) e estacao (str).
    Imprime o consumo médio de um determinado ano e estação.
    """
    consumo_medio = calcular_consumo_medio(ano, estacao)
    if consumo_medio is None:
        logging.error(f"Failed to calculate consumo médio for {ano} {estacao}")
    else:
        print(f"Consumo médio for {ano} {estacao}: {consumo_medio:.2f}")
    time.sleep(1)  # Wait for 1 second between requests

def main():
    """
    Esta é a função principal que controla a execução do programa.
    Define os anos e temporadas a serem processados ​​e chama a função process_year_season para cada combinação.
    """
    anos = [2021, 2022, 2023]
    estacoes = ['Outono', 'Inverno', 'Primavera', 'Verão']

    for ano in anos:
        for estacao in estacoes:
            process_year_season(ano, estacao)

if __name__ == "__main__":
    main()