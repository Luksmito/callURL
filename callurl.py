import requests

url = "https://:l-VrwV_BQC-XhdkhF6VYQA@tandem.autodesk.com/api/v1/timeseries/models/urn:adsk.dtm:65yT5kH4R42K6Op8xAP_uw/streams/AQAAAJsv-v3IAUEWpnJjjtkN0vMAAAAA"
data = [{"umidade": 37}]
response = requests.post(url, json=data)

