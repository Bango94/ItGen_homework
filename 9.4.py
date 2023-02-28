import string

def search(text:str):
    for item in string.punctuation:
        text = text.replace(item,'')
        return len(text.split())

print(search('hello world'))
