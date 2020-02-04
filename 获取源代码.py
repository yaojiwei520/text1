import requests
response = requests.get('https://baijiahao.baidu.com')
print(response.content.decode('UTF8'))
