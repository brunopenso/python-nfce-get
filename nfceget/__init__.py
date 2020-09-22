import app

class Nfceget(object):
    def __init__(self):
        pass

    @staticmethod
    def from_qrcode(link):
        return app.json_from_qrcode_link(link)

    @staticmethod
    def from_file(file):
        return app.json_from_file(file)
