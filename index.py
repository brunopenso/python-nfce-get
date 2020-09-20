from src import nfceHtml, StateInvalid
import urllib3
listOfStatesAvailableQrCode = ['pr.gov.br/nfce/qrcode']

def getJsonFromQrcodelink(link):
    for states in listOfStatesAvailableQrCode:
        if (states in link):
            http = urllib3.PoolManager()
            htmlData = http.request('GET', link).data
            return nfceHtml.getJsonFromHtml(htmlData)
    raise StateInvalid('According to link provided the state related to the domain is not available')

def getJsonFromFile(filePath):
    f = open(filePath, 'r')
    htmlData = f.read()
    return nfceHtml.getJsonFromHtml(htmlData)
