import json


with open('json/imobiliaria.json', encoding='utf-8') as file:
    data = json.load(file)

imoveis = data["imobiliaria"]["imovel"]


for id, imovel in enumerate(imoveis, start=1):
    print(f"{id} - {imovel['descricao']}")

print()


selecionado = int(input("Escolha o número do imóvel para ver detalhes: "))
imovel_escolhido = imoveis[selecionado - 1]


descricao = imovel_escolhido["descricao"]
proprietario = imovel_escolhido["proprietario"]
telefone = proprietario["telefone"]
email = proprietario.get("email", "Sem email disponível")
endereco = imovel_escolhido["endereco"]
caracteristicas = imovel_escolhido["caracteristicas"]
valor = imovel_escolhido["valor"]


print("Detalhes do Imóvel:")
print(f"Descrição: {descricao}\n")

print(f"Proprietário: {proprietario['nome']}\n")

print("telefone:")
telefones = telefone if isinstance(telefone, list) else [telefone]
for tel in telefones:
    print(f"- {tel}")

print(f"email: {email}\n")

print("localização:")
print(f"{endereco['rua']}")
print(f"{endereco['bairro']}")
print(f"{endereco['cidade']}")
print(f"{endereco['numero']}\n")

print("Características do Imóvel:")
print(f"{caracteristicas['tamanho']}")
print(f"{caracteristicas['numQuartos']}")
print(f"{caracteristicas['numBanheiros']}\n")

print(valor)