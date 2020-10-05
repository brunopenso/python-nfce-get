import json
import re
from ..util import clear_text, normalize_key, remove_numbers

from bs4 import Tag, NavigableString, BeautifulSoup

def fill_company_data(json, soup):
    div = soup.find(id="Emitente")
    tds = div.find_all('td')
    for td in tds:
        label = clear_text(td.find('label').get_text())
        value = clear_text(td.find('span').get_text())
        if (label == 'CNPJ'):
            json['local']['cnpj'] = value
        if (label == 'Nome / Razão Social'):
            json['local']['name'] = value
        if (label == 'Endereço'):
            json['local']['address'] = value
        if (label == 'Bairro / Distrito'):
            json['local']['address'] += " - " + value
        if (label == 'Município'):
            json['local']['address'] += " - " + remove_numbers(value)

def fill_itens(json, soup):
    div = soup.find(id="Prod")
    tables = div.find_all('table')
    for i in range(len(tables)):
        if (i == 0 or (i+1) >= len(tables)):
            continue
        table1 = tables[i]
        table2 = tables[i+1]
        if (table1 is None or table2 is None):
            continue
        classes1 = table1['class']
        classes2 = table2['class']
        if ('toggle' in classes1
            and 'box' in classes1
            and 'toggable' in classes2
            and 'box' in classes2):
            fill_item(json, tables[i], tables[i+1])

def fill_item(json, table1, table2):
    json_item = {}
    tds = table1.find_all('td')
    for column in tds:
        clazz = column['class'][0]
        value = clear_text(column.get_text())
        if (clazz == 'fixo-prod-serv-descricao'):
            json_item['name'] = value
        if (clazz == 'fixo-prod-serv-qtd'):
            json_item['quantity'] = value
        if (clazz == 'fixo-prod-serv-uc'):
            json_item['unit'] = value
        if (clazz == 'fixo-prod-serv-vb'):
            json_item['totalValue'] = value.strip()
    tds2 = table2.find_all('td')
    for column in tds2:
        if (column.find('label') == None):
            continue
        label = clear_text(column.find('label').get_text())
        value = clear_text(column.find('span').get_text())
        if (label == 'Código do Produto'):
            json_item['code'] = value
        if (label == 'Valor unitário de comercialização'):
            json_item['unitaryValue'] = value
    json['itens'].append(json_item)

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

    return json