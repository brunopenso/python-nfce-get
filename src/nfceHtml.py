import json
from bs4 import BeautifulSoup

def clearText(text):
    value = text.splitlines()
    value =  "".join(value).strip()
    value = value.replace('\t', '')
    return value

def getJsonFromHtml(data):
    json = {
        'local': {

        },
        'itens': []
    }

    soup = BeautifulSoup(data, 'html.parser')

    divConteudo = soup.find(id="conteudo")
    divs = divConteudo.find_all('div')
    place = divs[1].find_all('div')

    json['local']['name'] = clearText(place[0].get_text())
    json['local']['cnpj'] = clearText(place[1].get_text())
    json['local']['address'] = clearText(place[2].get_text())

    tableResult = soup.find(id="tabResult").find_all("tr")
    for row in tableResult:
        tds = row.find_all("td")
        jsonItem = {}
        for column in tds:
            spans = column.find_all('span')
            for span in spans:
                htmlValue = span.get_text()
                if (span['class'][0] == 'txtTit2'):
                    jsonItem['name'] = clearText(htmlValue)
                if (span['class'][0] == 'Rqtd'):
                    jsonItem['quantity'] = clearText(htmlValue).replace("Qtde.:", '')
                if (span['class'][0] == 'RUN'):
                    jsonItem['unit'] = clearText(htmlValue).replace("UN: ", '')
                if (span['class'][0] == 'RvlUnit'):
                    jsonItem['unitaryValue'] = clearText(htmlValue).replace("Vl. Unit.:", '')
        json['itens'].append(jsonItem)
    return json
