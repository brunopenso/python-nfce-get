import urllib3

def retrieveHtmlData(url):
    http = urllib3.PoolManager()
    return http.request('GET', url).data