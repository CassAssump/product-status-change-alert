import requests
from bs4 import BeautifulSoup
import time

def get_order_status(url, retries=3, delay=2):
    """
    Faz a requisição da URL do pedido e extrai o status atual, com tentativas de recuperação.
    
    Args:
        url (str): URL compartilhada do pedido.
        retries (int): Número de tentativas para capturar o status.
        delay (int): Tempo de espera entre as tentativas.

    Returns:
        str: Status atual do pedido ou "Status não encontrado" se falhar.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            '''ATENÇÃO: AQUI DEVE SER A LOCALIZAÇÃO DO ELEMENTO NA PÁGINA, MUDAR CASO NESCESSÁRIO'''
            status_element = soup.find('span', id='primaryStatus')
            
            if status_element:
                # Extrai o texto do status, ignorando o texto dentro de span interno (a data)
                status_text = status_element.get_text(separator=" ", strip=True)
                return status_text.strip()
            
        except Exception as e:
            print(f"Tentativa {attempt + 1} falhou: {e}")
        
        # Espera antes da próxima tentativa
        time.sleep(delay)
    
    return "Status não encontrado"

def track_order_status(url, check_interval=300):
    """
    Verifica o status do pedido periodicamente e notifica no console se houver mudança.
    
    Args:
        url (str): URL compartilhada do pedido.
        check_interval (int): Intervalo de verificação em segundos (padrão: 300 segundos).
    """
    last_status = None

    while True:
        try:
            current_status = get_order_status(url)
            
            if current_status != last_status and current_status != "Status não encontrado":
                print(f"Status do pedido mudou para: {current_status}")
                last_status = current_status
            elif current_status == "Status não encontrado":
                print("Não foi possível encontrar o status. Tentando novamente na próxima verificação.")
            else:
                print("Status do pedido não mudou.")
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

        time.sleep(check_interval)  # Espera pelo intervalo definido antes de verificar novamente

# Substitua 'sua_url_aqui' com a URL compartilhada do seu pedido Amazon
url = 'https://a.co/d/1Qamb20'
track_order_status(url, check_interval=1)
