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
def fill_company_data(soup):
    div_conteudo = soup.find(id="conteudo")
    divs = div_conteudo.find_all('div')
    place = divs[1].find_all('div')

    json['local']['name'] = clear_text(place[0].get_text())
    cnpj = clear_text(place[1].get_text())
    if ('CNPJ:' in cnpj):
        cnpj = cnpj.replace('CNPJ:','').strip()
    json['local']['cnpj'] = cnpj
    json['local']['address'] = clear_text(place[2].get_text())

def fill_itens(soup):
    table_result = soup.find(id="tabResult").find_all("tr")
    for row in table_result:
        tds = row.find_all("td")
        json_item = {}
        for column in tds:
            spans = column.find_all('span')
            for span in spans:
                html_value = span.get_text()
                if (span['class'][0] == 'txtTit2'):
                    json_item['name'] = clear_text(html_value)
                if (span['class'][0] == 'Rqtd'):
                    json_item['quantity'] = clear_text(html_value).replace("Qtde.:", '')
                if (span['class'][0] == 'RUN'):
                    json_item['unit'] = clear_text(html_value).replace("UN: ", '')
                if (span['class'][0] == 'RvlUnit'):
                    json_item['unitaryValue'] = clear_text(html_value).replace("Vl. Unit.:", '').strip()
                if (span['class'][0] == 'valor'):
                    json_item['totalValue'] = clear_text(html_value).strip()
        json['itens'].append(json_item)

def fill_nfce_totals(soup):
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

def fill_nfce_infos(soup):
    div_info = soup.find(id='infos')
    divs = div_info.find_all('div')
    for div in divs:
        h4_tag = div.find('h4')
        if (h4_tag is None):
            continue
        if (h4_tag.get_text() == 'Informações gerais da Nota'):
            fill_nfce_info_general(div)
        if (h4_tag is not None and h4_tag.get_text() == 'Chave de acesso'):
            key = div.find('span')
            json['nfce']['protocol'] = normalize_key(key.get_text())

def fill_nfce_info_general(div):
    lis = div.find('li')
    for li in lis:
        if (li is None or li == '\n'):
            continue
        if (isinstance(li, Tag)):
            if (li.get_text().strip() == 'Número:'):
                json['nfce']['numero'] = li.nextSibling.strip()
            if (li.get_text().strip() == 'Série:'):
                json['nfce']['serie'] = li.nextSibling.strip()
            if (li.get_text().strip() == 'Emissão:'):
                date_list = li.nextSibling.strip().split(' ')
                json['nfce']['date'] = date_list[0] + ' ' + date_list[1]
            if (li.get_text().strip() == 'Protocolo de Autorização:'):
                json['nfce']['protocol'] = li.nextSibling.strip()
            if ('Ambiente de Produção' in li.get_text()):
                value = li.get_text().split('-')
                json['nfce']['version'] = clear_text(value[1]).replace('Versão XML: ', '')

def get_json_from_html(data):
    soup = BeautifulSoup(data, 'html.parser')

    fill_company_data(soup)

    fill_itens(soup)

    fill_nfce_totals(soup)

    fill_nfce_infos(soup)

    return json