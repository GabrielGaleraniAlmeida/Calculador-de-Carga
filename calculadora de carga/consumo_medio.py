import requests
import pandas as pd
import logging
import time

# Configurar o log para registrar informações e erros em um arquivo de log
logging.basicConfig(filename='log.txt', level=logging.INFO)

def obter_dados_da_api(dat_inicio, dat_fim, cod_areacarga):
    """
    Esta função recupera dados da API para um período e código de área de carga específicos.
    São necessários três argumentos: dat_inicio (str), dat_fim (str), e cod_areacarga (int).
    Ela retorna a resposta da API no formato JSON se for bem-sucedida ou Nenhum se houver um erro.
    """
    url = f"http://ons-dl-prod-opendata-swagger.s3-website-us-east-1.amazonaws.com/?dat_inicio={dat_inicio}&dat_fim={dat_fim}&cod_areacarga={cod_areacarga}"
    try:
        resposta = requests.get(url)
        logging.info(f"Requesting {url}: {resposta.status_code}")
        if resposta.status_code != 200:
            logging.error(f"Failed to request {url}: {resposta.text}")
            return None
        return resposta.json()
    except requests.RequestException as e:
        logging.error(f"Error requesting {url}: {e}")
        return None

def calcular_consumo_medio(dat_inicio, dat_fim, cod_areacarga):
    """
    Esta função calcula o consumo médio para um período e código de área de carga específicos.
    São necessários três argumentos: dat_inicio (str), dat_fim (str), e cod_areacarga (int).
    Retorna o consumo médio se for bem-sucedido ou Nenhum se houver erro.
    """
    dados = obter_dados_da_api(dat_inicio, dat_fim, cod_areacarga)
    if dados is None:
        logging.error(f"Failed to get data for {dat_inicio} to {dat_fim} for area code {cod_areacarga}")
        return None
    consumo = [item['carga_global'] for item in dados]
    consumo_medio = sum(consumo) / len(consumo)
    logging.info(f"Consumo médio from {dat_inicio} to {dat_fim} for area code {cod_areacarga}: {consumo_medio:.2f}")
    return consumo_medio

def process_year_season(dat_inicio, dat_fim, cod_areacarga):
    """
    Esta função processa um único período e código de área de carga.
    São necessários três argumentos: dat_inicio (str), dat_fim (str), e cod_areacarga (int).
    Imprime o consumo médio para o período e área de carga especificados.
    """
    consumo_medio = calcular_consumo_medio(dat_inicio, dat_fim, cod_areacarga)
    if consumo_medio is None:
        logging.error(f"Failed to calculate consumo médio from {dat_inicio} to {dat_fim} for area code {cod_areacarga}")
    else:
        print(f"Consumo médio from {dat_inicio} to {dat_fim} for area code {cod_areacarga}: {consumo_medio:.2f}")
    time.sleep(1)  # Wait for 1 second between requests

def main():
    """
    Esta é a função principal que controla a execução do programa.
    Define os períodos e códigos de área de carga a serem processados e chama a função process_year_season para cada combinação.
    """
    periodos = [("2021-01-01", "2021-12-31"), ("2022-01-01", "2022-12-31"), ("2023-01-01", "2023-12-31")]
    codigos_areacarga = [1, 2, 3, 4]  # Exemplo de códigos de área de carga

    for periodo in periodos:
        for cod_areacarga in codigos_areacarga:
            process_year_season(periodo[0], periodo[1], cod_areacarga)

if __name__ == "__main__":
    main()
