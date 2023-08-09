import requests

def consultar_api_email(email):
    url = f'https://apisdedicado.nexos.dev/SerasaEmail/email?token=2ae274ad75c45b657547631a82358dbc&email={email}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None
