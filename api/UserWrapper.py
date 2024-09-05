import json

# Dados de usuários
users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    # Adicione aqui os outros usuários
]

def listar_usuarios():
    """Lista todos os usuários com ID, nome e username."""
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['name']}, Username: {user['username']}")

def exibir_usuario(user_id):
    """Exibe os detalhes de um usuário específico."""
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        print(json.dumps(user, indent=4))
    else:
        print("Usuário não encontrado.")

def criar_usuario():
    """Cria um novo usuário com dados fornecidos pelo usuário."""
    new_id = max(user["id"] for user in users) + 1
    name = input("Nome: ")
    username = input("Username: ")
    email = input("Email: ")

    new_user = {
        "id": new_id,
        "name": name,
        "username": username,
        "email": email,
        "address": {},
        "phone": "",
        "website": "",
        "company": {}
    }
    users.append(new_user)
    print("Usuário criado com sucesso.")

def atualizar_usuario(user_id):
    """Atualiza os dados de um usuário existente."""
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['name'] = input(f"Nome ({user['name']}): ") or user['name']
        user['username'] = input(f"Username ({user['username']}): ") or user['username']
        user['email'] = input(f"Email ({user['email']}): ") or user['email']
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

def deletar_usuario(user_id):
    """Remove um usuário da lista com base no ID."""
    global users
    users = [user for user in users if user['id'] != user_id]
    print("Usuário deletado com sucesso.")

def menu_principal():
    """Exibe o menu principal e lida com as escolhas do usuário."""
    while True:
        print("\nMenu:")
        print("1. Listar todos os usuários")
        print("2. Exibir detalhes de um usuário")
        print("3. Criar novo usuário")
        print("4. Atualizar um usuário")
        print("5. Deletar um usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            user_id = int(input("ID do usuário: "))
            exibir_usuario(user_id)
        elif opcao == "3":
            criar_usuario()
        elif opcao == "4":
            user_id = int(input("ID do usuário: "))
            atualizar_usuario(user_id)
        elif opcao == "5":
            user_id = int(input("ID do usuário: "))
            deletar_usuario(user_id)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()