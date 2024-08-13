# Amazon Order Status Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Requests](https://img.shields.io/badge/Requests-2.26.0-brightgreen)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.10.0-orange)

Este projeto é um script Python que monitora o status de um pedido em shopping online usando uma URL compartilhada e notifica quando o status muda.
Ainda em construção, bugs podem ser encontrados e sistemas aprimorados.

## Funcionalidades

- Monitora o status do pedido de forma periódica.
- Notifica no console sempre que o status do pedido mudar.
- Possui tentativas automáticas de captura do status em caso de falha temporária.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `requests`, `beautifulsoup4`

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/CassAssump/product-status-change-alertit
    ```

2. Instale as dependências:

    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1. Edite o arquivo `tracker.py` e substitua a variável `url` com a URL do seu pedido Amazon.
2. "status_element = soup.find('span', id='primaryStatus')" Você deve procurar na página de rastreio os elementos que são utilizados para mostrar o status, mude 'span" e "id" conforme.
3. Execute o script:

    ```bash
    python main.py
    ```

4. O script verificará o status do pedido a cada 5 minutos por padrão. Se o status mudar, uma mensagem será impressa no console.

## Configuração

Você pode ajustar o intervalo de verificação e o número de tentativas automáticas editando os seguintes parâmetros no código:

- `check_interval`: Intervalo de verificação em segundos (padrão: 300 segundos).
- `retries`: Número de tentativas para capturar o status em caso de falha (padrão: 3 tentativas).
- `delay`: Tempo de espera entre as tentativas em segundos (padrão: 2 segundos).

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.


