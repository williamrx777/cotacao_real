from flask import Flask,render_template,url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    cotacao = requests.get(f"https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_euro = cotacao['EURBRL']['bid']
    z = float(cotacao_dolar)
    y = float(cotacao_euro)
    va  = (f'{z:.2f}')
    vi = (f'{y:.2f}')
    return render_template('index.html',va=va,vi=vi)

if __name__ == '__main__':
    app.run(debug=True)