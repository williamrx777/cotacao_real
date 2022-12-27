from flask import Flask,render_template,url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    cotacao = requests.get(f"https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_euro = cotacao['EURBRL']['bid']
    return render_template('index.html',cotacao_dolar=cotacao_dolar,cotacao_euro=cotacao_euro)

if __name__ == '__main__':
    app.run(debug=True)