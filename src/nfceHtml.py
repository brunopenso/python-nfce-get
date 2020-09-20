import json
from util import clear_text, normalize_key

from bs4 import Tag, NavigableString, BeautifulSoup

json = {
    'local': {
    },
    'itens': [],
    'totals': {
    },
    'nfce': {
    }
}
def fillCompanyData(soup):
    divConteudo = soup.find(id="conteudo")
    divs = divConteudo.find_all('div')
    place = divs[1].find_all('div')

    json['local']['name'] = clear_text(place[0].get_text())
    cnpj = clear_text(place[1].get_text())
    if ('CNPJ:' in cnpj):
        cnpj = cnpj.replace('CNPJ:','').strip()
    json['local']['cnpj'] = cnpj
    json['local']['address'] = clear_text(place[2].get_text())

def fillItens(soup):
    tableResult = soup.find(id="tabResult").find_all("tr")
    for row in tableResult:
        tds = row.find_all("td")
        jsonItem = {}
        for column in tds:
            spans = column.find_all('span')
            for span in spans:
                htmlValue = span.get_text()
                if (span['class'][0] == 'txtTit2'):
                    jsonItem['name'] = clear_text(htmlValue)
                if (span['class'][0] == 'Rqtd'):
                    jsonItem['quantity'] = clear_text(htmlValue).replace("Qtde.:", '')
                if (span['class'][0] == 'RUN'):
                    jsonItem['unit'] = clear_text(htmlValue).replace("UN: ", '')
                if (span['class'][0] == 'RvlUnit'):
                    jsonItem['unitaryValue'] = clear_text(htmlValue).replace("Vl. Unit.:", '').strip()
                if (span['class'][0] == 'valor'):
                    jsonItem['totalValue'] = clear_text(htmlValue).strip()
        json['itens'].append(jsonItem)

def fillNfceTotals(soup):
    totals = soup.find(id="totalNota")
    divs = totals.find_all('div')
    for div in divs:
        label = clear_text(div.find('label').get_text())
        value = clear_text(div.find('span').get_text())
        if (label == 'Qtd. total de itens:'):
            json['totals']['quantityItens'] = value
        if (label == 'Valor total R$:'):
            json['totals']['total'] = value
        if (label == 'Descontos R$:'):
            json['totals']['discounts'] = value
        if ('nformação dos Tributos Totais Incidentes' in label):
            json['totals']['taxes'] = value
        if (label == 'Valor a pagar R$:'):
            json['totals']['valueToPay'] = value

def fillNfceInfos(soup):
    divInfo = soup.find(id='infos')
    divs = divInfo.find_all('div')
    for div in divs:
        h4Tag = div.find('h4')
        if (h4Tag is not None and h4Tag.get_text() == 'Informações gerais da Nota'):
            lis = div.find('li')
            for li in lis:
                if (li is not None and li != '\n' and isinstance(li, Tag)):
                    if (li.get_text().strip() == 'Número:'):
                        json['nfce']['numero'] = li.nextSibling.strip()
                    if (li.get_text().strip() == 'Série:'):
                        json['nfce']['serie'] = li.nextSibling.strip()
                    if (li.get_text().strip() == 'Emissão:'):
                        dateList = li.nextSibling.strip().split(' ')
                        json['nfce']['date'] = dateList[0] + ' ' + dateList[1]
                    if (li.get_text().strip() == 'Protocolo de Autorização:'):
                        json['nfce']['protocol'] = li.nextSibling.strip()
                    if ('Ambiente de Produção' in li.get_text()):
                        value = li.get_text().split('-')
                        json['nfce']['version'] = clear_text(value[1]).replace('Versão XML: ', '')
        if (h4Tag is not None and h4Tag.get_text() == 'Chave de acesso'):
            key = div.find('span')
            json['nfce']['protocol'] = normalize_key(key.get_text())

def getJsonFromHtml(data):
    soup = BeautifulSoup(data, 'html.parser')

    fillCompanyData(soup)

    fillItens(soup)

    fillNfceTotals(soup)

    fillNfceInfos(soup)

    return json