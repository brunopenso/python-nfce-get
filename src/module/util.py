def normalize_key(key):
    if key is None:
        return ''
    key = key.split(' ')
    key = "".join(key).strip()
    return key

def clear_text(text):
    if text is None:
        return ''
    value = text.splitlines()
    value =  "".join(value).strip()
    value = value.replace('\t', '')
    return value.strip()
