import requests
from xml.dom.minidom import parseString

# URL e headers do serviço web
URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
HEADERS = {'Content-Type': 'text/xml; charset=utf-8'}

def obter_capital_pais(codigo_pais):
    """Obtém a capital do país usando o código ISO do país."""
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{codigo_pais}</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
                </soap:Envelope>"""

    try:
        response = requests.post(URL, headers=HEADERS, data=payload)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        context = parseString(response.content)
        capital = context.getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
        return capital
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar a resposta: {e}")
        return None

def numero_para_texto(numero):
    """Converte um número específico para seu equivalente em texto em inglês."""
    tabela_numeros = {
        212: "two hundred twelve",
        213: "two hundred thirteen",
        214: "two hundred fourteen",
        215: "two hundred fifteen",
        216: "two hundred sixteen",
        217: "two hundred seventeen",
        218: "two hundred eighteen",
        219: "two hundred nineteen",
        220: "two hundred twenty",
        221: "two hundred twenty-one",
        222: "two hundred twenty-two",
        223: "two hundred and twenty-three"
    }
    return tabela_numeros.get(numero, "Número não está na tabela!")

def main():
    # Exibir a capital da Noruega
    codigo_pais_noruega = "NO"
    capital_noruega = obter_capital_pais(codigo_pais_noruega)
    if capital_noruega:
        print(f"A capital da Noruega é: {capital_noruega}")
    
    # Converter número para texto
    try:
        numero = int(input("Digite um número de 212 a 223: "))
        if 212 <= numero <= 223:
            numero_extenso = numero_para_texto(numero)
            print(f"O número {numero} por extenso em inglês é: {numero_extenso}")
        else:
            print("Número fora do intervalo permitido!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
