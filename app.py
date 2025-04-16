from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)


def gerar_site_estatico():
    # Configura caminhos
    caminho_excel = os.path.join('data', 'dados.xlsx')
    caminho_saida = os.path.join('docs', 'index.html')

    # Processa o Excel
    df = pd.read_excel(caminho_excel)
    tabela_html = df.to_html(classes='tabela-excel', index=False)

    # Gera HTML estático
    with app.app_context():
        html = render_template('index.html', tabela=tabela_html)
        os.makedirs('docs', exist_ok=True)
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(html)


if __name__ == '__main__':
    gerar_site_estatico()
    print("Site estático gerado em docs/index.html")