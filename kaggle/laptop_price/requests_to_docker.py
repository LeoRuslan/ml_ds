import requests

# url = 'http://localhost:9696/predict'
url = 'http://18.119.11.120:9696/predict'

example = {'company': 'asus', 'product': 'ux430uq-gv209r (i7-7500u/8gb/256gb/geforce', 'typename': 'ultrabook', 'inches': 14.0, 'screenresolution': 'ips panel full hd 1920x1080', 'cpu': 'intel core i7 7500u 2.7ghz', 'ram': '8gb', 'memory': '256gb ssd', 'gpu': 'nvidia geforce 940mx', 'opsys': 'windows 10', 'weight': '1.3kg', 'price_euros': 1193.0}
res = requests.post(url=url, json=example).json()
print(res)
