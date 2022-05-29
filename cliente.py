import urllib.request

print('\n')

with urllib.request.urlopen("http://127.0.0.1:5000/") as url:
    response = url.read()
    print(response)

print('\n')
