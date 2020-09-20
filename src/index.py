import urllib3
from lib.nfceHtml import get_json_from_html
from lib import StateInvalid

listOfStatesAvailableQrCode = ['pr.gov.br/nfce/qrcode']

def json_from_qrcode_link(link):
    for states in listOfStatesAvailableQrCode:
        if (states in link):
            http = urllib3.PoolManager()
            html_data = http.request('GET', link).data
            return get_json_from_html(html_data)
    raise StateInvalid('According to link provided the state related to the domain is not available')

def json_from_file(file_path):
    f = open(file_path, 'r')
    html_data = f.read()
    return get_json_from_html(html_data)
