import urllib3
from nfceHtml import getJsonFromHtml
listOfStatesAvailableQrCode = ['pr.gov.br/nfce/qrcode']

def json_from_qrcode_link(link):
    for states in listOfStatesAvailableQrCode:
        if (states in link):
            http = urllib3.PoolManager()
            html_data = http.request('GET', link).data
            return getJsonFromHtml(html_data)
    raise StateInvalid('According to link provided the state related to the domain is not available')

def json_from_file(filePath):
    f = open(filePath, 'r')
    htmlData = f.read()
    return getJsonFromHtml(htmlData)

print(json_from_qrcode_link('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41200976430438005300650150002022071015187452|2|1|1|E9C67EF7E8B75CD401B3F6D3B1FD716ED22B3890'))