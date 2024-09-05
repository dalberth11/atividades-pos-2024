import requests

def exibir_opcoes():
    print("Opções:")
    print("1 - Ver todos os usuários")
    print("2 - Ver tarefas de um usuário")
    print("3 - Operações com usuários (CRUD)")

def obter_usuarios():
    resposta = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for usuario in resposta:
        print(f"{usuario['id']} - {usuario['username']}")

def obter_tarefas(usuario_id):
    tarefas = requests.get(f'https://jsonplaceholder.typicode.com/users/{usuario_id}/todos').json()
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa['title']}")

def criar_usuario():
    nome_usuario = input("Nome do usuário: ")
    novo_usuario = {
        "name": nome_usuario,
        "username": nome_usuario,
        "email": "exemplo@dominio.com"
    }
    resposta = requests.post('https://jsonplaceholder.typicode.com/users', json=novo_usuario)
    print(f"Usuário criado: {resposta.json()}")

def ler_usuario(usuario_id):
    resposta = requests.get(f'https://jsonplaceholder.typicode.com/users/{usuario_id}').json()
    print(f"Usuário {usuario_id}: {resposta}")

def atualizar_usuario(usuario_id):
    novo_nome = input("Novo nome do usuário: ")
    resposta = requests.patch(f'https://jsonplaceholder.typicode.com/users/{usuario_id}', json={"username": novo_nome})
    print(f"Usuário atualizado: {resposta.json()}")

def deletar_usuario(usuario_id):
    resposta = requests.delete(f'https://jsonplaceholder.typicode.com/users/{usuario_id}')
    print(f"Usuário deletado: {resposta.status_code}")

def operacoes_crud():
    print("1 - Criar usuário")
    print("2 - Ler usuário")
    print("3 - Atualizar usuário")
    print("4 - Deletar usuário")

    escolha_crud = input("Escolha uma ação: ")

    if escolha_crud == '1':
        criar_usuario()
    elif escolha_crud == '2':
        usuario_id = input("Informe o ID do usuário: ")
        ler_usuario(usuario_id)
    elif escolha_crud == '3':
        usuario_id = input("Informe o ID do usuário: ")
        atualizar_usuario(usuario_id)
    elif escolha_crud == '4':
        usuario_id = input("Informe o ID do usuário: ")
        deletar_usuario(usuario_id)

def main():
    exibir_opcoes()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        obter_usuarios()
    elif opcao == '2':
        usuario_id = input("Informe o ID do usuário: ")
        obter_tarefas(usuario_id)
    elif opcao == '3':
        operacoes_crud()

if __name__ == "__main__":
    main()