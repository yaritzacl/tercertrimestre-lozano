import requests
url='https://api.github.com/users'
sesion=requests.session()
sesion.auth=('zully9888@gmail.com','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'
)
response=sesion.get(url)

if response.status_code==200:
    response1=sesion.get ('https://github.com/yaritzacl')
    print(response1.cookies)
    print(response.content)
