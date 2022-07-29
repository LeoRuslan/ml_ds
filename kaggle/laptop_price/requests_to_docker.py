import requests

url = 'http://localhost:9696/predict'

example = {'company': 'asus', 'product': 'zenbook flip', 'typename': '2 in 1 convertible', 'inches': 13.3, 'screenresolution': 'ips panel full hd / touchscreen 1920x1080', 'cpu': 'intel core i5 7200u 2.5ghz', 'ram': '8gb', 'memory': '256gb ssd', 'gpu': 'intel hd graphics 620', 'opsys': 'windows 10', 'weight': '1.27kg', 'price_euros': 928.0}
res = requests.post(url=url, json=example).json()
print(res)
