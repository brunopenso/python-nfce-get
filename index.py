import urllib3
import json

from bs4 import BeautifulSoup

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.fazenda.pr.gov.br/nfce/qrcode?p=41200976430438005300650150002022071015187452|2|1|1|E9C67EF7E8B75CD401B3F6D3B1FD716ED22B3890')

def clear_html(text):
    value = text.splitlines()
    value =  "".join(value).strip()
    value = value.replace('\t', '')
    return value

json = {
    'local': {

    },
    'itens': []
}

soup = BeautifulSoup(r.data, 'html.parser')

divConteudo = soup.find(id="conteudo")
divs = divConteudo.find_all('div')
place = divs[1].find_all('div')

json['local']['name'] = clear_html(place[0].get_text())
json['local']['cnpj'] = clear_html(place[1].get_text())
json['local']['address'] = clear_html(place[2].get_text())

tableResult = soup.find(id="tabResult").find_all("tr")
for row in tableResult:
    tds = row.find_all("td")
    jsonItem = {}
    for column in tds:
        spans = column.find_all('span')
        for span in spans:
            htmlValue = span.get_text()
            if (span['class'][0] == 'txtTit2'):
                jsonItem['name'] = clear_html(htmlValue)
            if (span['class'][0] == 'Rqtd'):
                jsonItem['quantity'] = clear_html(htmlValue).replace("Qtde.:", '')
            if (span['class'][0] == 'RUN'):
                jsonItem['unit'] = clear_html(htmlValue).replace("UN: ", '')
            if (span['class'][0] == 'RvlUnit'):
                jsonItem['unitaryValue'] = clear_html(htmlValue).replace("Vl. Unit.:", '')
    json['itens'].append(jsonItem)

print(json)