# Amazon Order Status Tracker

Este projeto é um script Python que monitora o status de um pedido na Amazon usando uma URL compartilhada e notifica quando o status muda.


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
    git clone https://github.com/CassAssump/product-status-change-alert
    ```

2. Instale as dependências:

    ```bash
    pip install requests beautifulsoup4
    ```

## Uso

1. Edite o arquivo `tracker.py` e substitua a variável `url` com a URL do seu pedido Amazon.
2. Execute o script:

    ```bash
    python main.py
    ```

3. O script verificará o status do pedido a cada 5 minutos por padrão. Se o status mudar, uma mensagem será impressa no console.

## Configuração

Você pode ajustar o intervalo de verificação e o número de tentativas automáticas editando os seguintes parâmetros no código:

- `check_interval`: Intervalo de verificação em segundos (padrão: 300 segundos).
- `retries`: Número de tentativas para capturar o status em caso de falha (padrão: 3 tentativas).
- `delay`: Tempo de espera entre as tentativas em segundos (padrão: 2 segundos).

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

