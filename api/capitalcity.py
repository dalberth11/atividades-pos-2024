import requests
from xml.dom.minidom import parseString

# URL do serviço web
URL = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
HEADERS = {'Content-Type': 'text/xml; charset=utf-8'}

def enviar_requisicao(payload):
    """Envia uma requisição SOAP e retorna o conteúdo da resposta."""
    response = requests.post(URL, headers=HEADERS, data=payload)
    return response.content

def obter_dado_pais(acao, country_code):
    """Obtém um dado do país usando o código ISO do país e a ação desejada."""
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <{acao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </{acao}>
                </soap:Body>
                </soap:Envelope>"""

    response_content = enviar_requisicao(payload)
    context = parseString(response_content)
    result_tag = f'm:{acao}Result'
    
    if acao == "CountryCurrency":
        # Para CountryCurrency, precisamos buscar um filho específico
        return context.getElementsByTagName('m:sISOCode')[0].firstChild.nodeValue
    else:
        return context.getElementsByTagName(result_tag)[0].firstChild.nodeValue

def obter_capital_pais(country_code):
    """Obtém a capital do país usando o código ISO do país."""
    return obter_dado_pais("CapitalCity", country_code)

def obter_moeda_pais(country_code):
    """Obtém a moeda do país usando o código ISO do país."""
    return obter_dado_pais("CountryCurrency", country_code)

def obter_codigo_telefone_pais(country_code):
    """Obtém o código de telefone do país usando o código ISO do país."""
    return obter_dado_pais("CountryIntPhoneCode", country_code)

# Código do país para consulta
codigo_pais = "NZ"

capital = obter_capital_pais(codigo_pais)
print(f"A capital da {codigo_pais} é: {capital}")

moeda = obter_moeda_pais(codigo_pais)
codigo_telefone = obter_codigo_telefone_pais(codigo_pais)

print(f"A moeda local é: {moeda}")
print(f"Código de telefone do país: +{codigo_telefone}")