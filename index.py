from src import util
from src import nfceHtml

htmlData = util.retrieveHtmlData('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41200976430438005300650150002022071015187452|2|1|1|E9C67EF7E8B75CD401B3F6D3B1FD716ED22B3890')

jsonData = nfceHtml.getJsonFromHtml(htmlData)

print(jsonData)