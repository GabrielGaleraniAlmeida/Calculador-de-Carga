
Consumo de Energia Elétrica - Análise de Dados

Este é um programa Python para análise do consumo de energia elétrica, utilizando dados disponíveis na API do Operador Nacional do Sistema Elétrico (ONS). Ele calcula o consumo médio para períodos e códigos de área de carga específicos, fornecendo informações úteis para entender os padrões de consumo ao longo do tempo e em diferentes regiões.

 Pré-requisitos
- Python 3.x
- Bibliotecas: `requests`, `pandas`

Instalação
1. Certifique-se de ter Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/).
2. Instale as dependências necessárias executando `pip install requests pandas`.

Utilização
1. Clone o repositório ou baixe o arquivo `codigo.py`.
2. No diretório do projeto, execute `python codigo.py`.
3. Os resultados serão exibidos no terminal e registrados em um arquivo de log chamado `log.txt`.

Funcionalidades
- **Obtenção de Dados da API**: A função `obter_dados_da_api(dat_inicio, dat_fim, cod_areacarga)` busca dados da API do ONS para um período e código de área de carga específicos.
- **Cálculo do Consumo Médio**: A função `calcular_consumo_medio(dat_inicio, dat_fim, cod_areacarga)` calcula o consumo médio com base nos dados obtidos da API.
- **Processamento por Período e Código de Área de Carga**: A função `process_year_season(dat_inicio, dat_fim, cod_areacarga)` processa um único período e código de área de carga, exibindo o consumo médio.
- **Função Principal**: A função `main()` controla a execução do programa, definindo os períodos e códigos de área de carga a serem processados e chamando a função `process_year_season` para cada combinação.

