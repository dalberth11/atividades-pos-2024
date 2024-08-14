from xml.dom.minidom import parse

dom = parse ("parse/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")

for prato in pratos:
    
    prato_id = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f" Prato {prato_id }: {nome}")  
 

prato_id = int(input("DIGITE O ID DO PRATO/CARDAPIO: "))
prato = pratos [prato_id]

descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue 
ingredientes = prato.getElementsByTagName("ingrediente")
ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in ingredientes]
preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue 
calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue 
tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue 


print(f"Nome do Prato: {nome}")
print(f"Descrição do Prato: {descricao}")
print(f"Ingredientes:")
print(f"\n".join(ingredientes))
print(f"Preço do Prato: R${preco}")
print(f"Calorias do Prato: {calorias} Kilocaloria")
print(f"Tempo de Preparo: {tempoPreparo}")

