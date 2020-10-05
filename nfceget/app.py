import urllib3
from .htmlNfce import run
from .StateInvalidError import StateInvalidError

listOfStatesAvailableQrCode = ['pr.gov.br/nfce/qrcode']

def json_from_qrcode_link(link):
    if (link is None or len(link.strip()) == 0):
        raise ValueError('Please inform a valid NFCE url')
    for states in listOfStatesAvailableQrCode:
        if (states in link):
            http = urllib3.PoolManager()
            html_data = http.request('GET', link).data
            return run('notaparana', html_data)
    raise StateInvalidError('De acordo com o link informado o estado não é suportado. Por favor consulte a documentação para verificar quais estados estão disponíveis.')

def json_from_file(file_path):
    f = open(file_path, 'r')
    html_data = f.read()
    f.close()
    if ( "Consulta da NF-e" not in html_data):
        return run("notaparana", html_data)

    return run("receitaestadualpr", html_data)

