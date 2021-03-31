import json
import re
from ..util import clear_text, normalize_key, remove_numbers
from ..QrCodeLinkNotFound import QrCodeLinkNotFound
from bs4 import Tag, NavigableString, BeautifulSoup

def get_qr_code(data):
    soup = BeautifulSoup(data, 'html.parser')
    divInf = soup.find(id="Inf")
    divs = divInf.find_all('td')
    for div in divs:
        label = div.find('label')
        if (label.get_text() == "QR-Code"):
            span = div.find('span')
            return span.get_text()

    raise QrCodeLinkNotFound('Não foi possível encontrar a url do qr code no arquivo da receita estadual')