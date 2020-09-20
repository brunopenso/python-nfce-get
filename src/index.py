import urllib3
from module.nfceHtml import get_json_from_html
from module.CustomEx import StateInvalidException

listOfStatesAvailableQrCode = ['pr.gov.br/nfce/qrcode']

def json_from_qrcode_link(link):
    if (link is None or len(link.strip()) == 0):
        raise Exception('Please inform a valid NFCE url')
    for states in listOfStatesAvailableQrCode:
        if (states in link):
            http = urllib3.PoolManager()
            html_data = http.request('GET', link).data
            return get_json_from_html(html_data)
    raise StateInvalidException('According to link provided the state related to the domain is not available')

def json_from_file(file_path):
    f = open(file_path, 'r')
    html_data = f.read()
    return get_json_from_html(html_data)
