from src import nfceHtml
import urllib3

def getJsonFromQrcodelink(link):
    http = urllib3.PoolManager()
    htmlData = http.request('GET', link).data
    return nfceHtml.getJsonFromHtml(htmlData)

def getJsonFromFile(filePath):
    f = open(filePath, 'r')
    htmlData = f.read()
    return nfceHtml.getJsonFromHtml(htmlData)
