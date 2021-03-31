from .pr.notaparana import get_json_from_html as notaparana
from .pr.receitaestadual import get_qr_code as receitaestadualpr
import urllib3

def run(local, data):
    if (local == 'notaparana'):
        return notaparana(data)
    if (local == 'receitaestadualpr'):
        linkQrCode = receitaestadualpr(data)
        http = urllib3.PoolManager()
        html_data = http.request('GET', linkQrCode).data   
        return notaparana(html_data)
