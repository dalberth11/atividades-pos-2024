from xml.dom.minidom import parse

dom = parse("parse/cardapio.xml")
cardapio = dom.documentElement
pratos_cardapio = cardapio.getElementsByTagName("prato")

for prato in pratos_cardapio:
    
    id_cardapio = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f" Prato {id_cardapio }: {nome}")  
 

prato_id = int(input("DIGITE O ID DO PRATO/CARDAPIO: "))
prato = pratos_cardapio [prato_id]

Descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue 
ingredientes = prato.getElementsByTagName("ingrediente")
ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in ingredientes]
preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue 
calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue 
tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue 


print(f"nome: {nome}")
print(f"Descrição: {Descricao}")
print(f"Ingredientes:")
print(f"\n".join(ingredientes))
print(f"Preço: R${preco}")
print(f"Calorias: {calorias} Kilocaloria")
print(f"Tempo de Preparo: {tempoPreparo}")
