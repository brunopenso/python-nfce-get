import urllib3

def normalize_key(key):
    key = key.split(' ')
    key = "".join(key).strip()
    return key

def clear_text(text):
    value = text.splitlines()
    value =  "".join(value).strip()
    value = value.replace('\t', '')
    return value.strip()
