from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def exibir_excel():
    # Carrega o arquivo Excel
    caminho_excel = "data/dados.xlsx"
    df = pd.read_excel(caminho_excel)

    # Converte para HTML
    tabela_html = df.to_html(classes='tabela-excel', index=False)

    return render_template('index.html', tabela=tabela_html)


if __name__ == '__main__':
    app.run(debug=True)