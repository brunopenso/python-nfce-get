import urllib3

def normalizeKey(key):
    key = key.split(' ')
    key = "".join(key).strip()
    return key

def clearText(text):
    value = text.splitlines()
    value =  "".join(value).strip()
    value = value.replace('\t', '')
    return value.strip()
