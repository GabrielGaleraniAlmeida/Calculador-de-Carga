
Consumo de Energia Elétrica - Análise de Dados
Este é um programa Python para análise do consumo de energia elétrica, utilizando dados disponíveis na API do Operador Nacional do Sistema Elétrico (ONS). Ele calcula o consumo médio para anos e estações específicos, fornecendo informações úteis para entender os padrões de consumo ao longo do tempo.

Pré-requisitos
Python 3.x
Bibliotecas: requests, pandas
Instalação
Certifique-se de ter Python instalado. Você pode baixá-lo em python.org.
Instale as dependências necessárias executando pip install requests pandas.
Utilização
Clone o repositório ou baixe o arquivo codigo.py.
No diretório do projeto, execute python codigo.py.
Os resultados serão exibidos no terminal e registrados em um arquivo de log chamado log.txt.
Funcionalidades
Obtenção de Dados da API: A função obter_dados_da_api(ano, estacao) busca dados da API do ONS para um ano e estação específicos.
Cálculo do Consumo Médio: A função calcular_consumo_medio(ano, estacao) calcula o consumo médio com base nos dados obtidos da API.
Processamento por Ano e Estação: A função process_year_season(ano, estacao) processa um único ano e estação, exibindo o consumo médio.
Função Principal: A função main() controla a execução do programa, definindo os anos e estações a serem processados e chamando a função process_year_season para cada combinação.
