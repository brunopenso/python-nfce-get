import json
import re
from ..util import clear_text, normalize_key

from bs4 import Tag, NavigableString, BeautifulSoup

def fill_company_data(json, soup):
    div_conteudo = soup.find(id="conteudo")
    divs = div_conteudo.find_all('div')
    place = divs[1].find_all('div')

    json['local']['name'] = clear_text(place[0].get_text())
    cnpj = clear_text(place[1].get_text())
    if ('CNPJ:' in cnpj):
        cnpj = cnpj.replace('CNPJ:','').strip()
    json['local']['cnpj'] = cnpj
    json['local']['address'] = clear_text(place[2].get_text())

def fill_itens(json, soup):
    table_result = soup.find(id="tabResult").find_all("tr")
    for row in table_result:
        tds = row.find_all("td")
        fill_itens_item(json, tds)

def fill_itens_item(json, tds):
    json_item = {}
    for column in tds:
        spans = column.find_all('span')
        for span in spans:
            value = clear_text(span.get_text())
            clazz = span['class'][0]
            if (clazz == 'txtTit2'):
                json_item['name'] = value
            if (clazz == 'Rqtd'):
                json_item['quantity'] = value.replace("Qtde.:", '')
            if (clazz == 'RUN'):
                json_item['unit'] = value.replace("UN: ", '')
            if (clazz == 'RvlUnit'):
                json_item['unitaryValue'] = value.replace("Vl. Unit.:", '').strip()
            if (clazz == 'valor'):
                json_item['totalValue'] = value.strip()
            if (clazz == 'RCod'):
                json_item['code'] = re.findall(r"\d+", value )[0]
    json['itens'].append(json_item)

def fill_nfce_totals(json, soup):
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

def fill_nfce_infos(json, soup):
    div_info = soup.find(id='infos')
    divs = div_info.find_all('div')
    for div in divs:
        h4_tag = div.find('h4')
        if (h4_tag is None):
            continue
        if (h4_tag.get_text() == 'Informações gerais da Nota'):
            fill_nfce_info_general(json, div)
        if (h4_tag is not None and h4_tag.get_text() == 'Chave de acesso'):
            key = div.find('span')
            json['nfce']['chave'] = normalize_key(key.get_text())

def fill_nfce_info_general(json, div):
    lis = div.find('li')
    for li in lis:
        if (li is None or li == '\n'):
            continue
        if (isinstance(li, Tag)):
            value = li.get_text().strip()
            if (value == 'Número:'):
                json['nfce']['numero'] = li.nextSibling.strip()
            if (value == 'Série:'):
                json['nfce']['serie'] = li.nextSibling.strip()
            if (value == 'Emissão:'):
                date_list = li.nextSibling.strip().split(' ')
                json['nfce']['date'] = date_list[0] + ' ' + date_list[1]
            if (value == 'Protocolo de Autorização:'):
                json['nfce']['protocolo'] = li.nextSibling.strip().split(' ')[0]
            if ('Ambiente de Produção' in li.get_text()):
                value = li.get_text().split('-')
                json['nfce']['version'] = clear_text(value[1]).replace('Versão XML: ', '')

def get_json_from_html(data):
    json = {
        'local': {
        },
        'itens': [],
        'totals': {
        },
        'nfce': {
        }
    }
    soup = BeautifulSoup(data, 'html.parser')

    fill_company_data(json, soup)

    fill_itens(json, soup)

    fill_nfce_totals(json, soup)

    fill_nfce_infos(json, soup)

    return json