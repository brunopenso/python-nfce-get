from .pr.notaparana import get_json_from_html as notaparana
from .pr.receitaestadual import get_json_from_html as receitaestadual

def run(local, data):
    if (local == 'notaparana'):
        return notaparana(data)
    if (local == 'receitaestadualpr'):
        return receitaestadual(data)
