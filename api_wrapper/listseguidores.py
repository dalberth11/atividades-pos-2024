import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

# Configurações iniciais
BASE_URL = 'https://api.github.com'
MENU_OPCOES = """
Opções:
1. Listar seguidores do usuário
2. Seguir um usuário
3. Parar de seguir um usuário
4. Voltar
"""

def obter_autenticacao():
    """Solicita e retorna as credenciais de autenticação do usuário."""
    user = input("Seu usuário do GitHub: ")
    password = getpass("Digite sua chave de acesso: ")
    return HTTPBasicAuth(user, password)

def listar_seguidores(usuario, auth):
    """Lista os seguidores de um usuário específico."""
    url = f'{BASE_URL}/users/{usuario}/followers'
    response = requests.get(url, auth=auth)
    
    if response.status_code == 200:
        seguidores = response.json()
        for seguidor in seguidores:
            print(seguidor['login'])
        print(f"Total de seguidores de {usuario}: {len(seguidores)}")
    else:
        print(f"Erro ao obter dados: {response.status_code} - {response.reason}")

def seguir_usuario(usuario, auth):
    """Segue um usuário específico."""
    url = f'{BASE_URL}/user/following/{usuario}'
    response = requests.put(url, auth=auth)
    
    if response.status_code == 204:
        print(f"Você agora está seguindo {usuario}.")
    else:
        print(f"Erro ao seguir o usuário: {response.status_code} - {response.reason}")

def parar_de_seguir_usuario(usuario, auth):
    """Para de seguir um usuário específico."""
    url = f'{BASE_URL}/user/following/{usuario}'
    response = requests.delete(url, auth=auth)
    
    if response.status_code == 204:
        print(f"Certo! Você deixou de seguir {usuario}.")
    else:
        print(f"Erro ao parar de seguir: {response.status_code} - {response.reason}")

def main():
    auth = obter_autenticacao()

    while True:
        print(MENU_OPCOES)
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            usuario = input("Digite o Nome do usuário para ver seus seguidores: ")
            listar_seguidores(usuario, auth)

        elif opcao == '2':
            usuario = input("Digite o login do usuário que deseja seguir: ")
            seguir_usuario(usuario, auth)

        elif opcao == '3':
            usuario = input("Digite o login do usuário que deseja deixar de seguir: ")
            parar_de_seguir_usuario(usuario, auth)

        elif opcao == '4':
            print("Valeu!")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()