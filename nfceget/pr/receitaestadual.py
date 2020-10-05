import json
import re
from ..util import clear_text, normalize_key

from bs4 import Tag, NavigableString, BeautifulSoup

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

    return json