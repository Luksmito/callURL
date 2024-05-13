from flask import Flask, request
import requests
import os

app = Flask(__name__)

# URL para onde será feita a requisição
url = "https://:l-VrwV_BQC-XhdkhF6VYQA@tandem.autodesk.com/api/v1/timeseries/models/urn:adsk.dtm:65yT5kH4R42K6Op8xAP_uw/streams/AQAAAJsv-v3IAUEWpnJjjtkN0vMAAAAA"

@app.route("/")

def hello():
    return "hello"
@app.route('/receber_numero', methods=['POST'])
def receber_numero():
    # Obtém o número do corpo da requisição
    numero = request.form.get('numero')
    
    # Constrói o corpo da nova requisição
    data = [{"umidade": numero}]
    
    # Faz a requisição para a URL fornecida
    response = requests.post(url, json=data)
    
    # Retorna a resposta da requisição feita para a URL
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))   