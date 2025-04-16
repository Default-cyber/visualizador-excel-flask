from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['APPLICATION_ROOT'] = '/'
app.config['PREFERRED_URL_SCHEME'] = 'http'

def gerar_site_estatico():
    try:
        # Carregar e processar dados
        caminho_excel = os.path.join('data', 'dados.xlsx')
        caminho_saida = os.path.join('docs', 'index.html')

        df = pd.read_excel(caminho_excel)
        df = df.fillna('')  # Corrigido aqui

        # Converter para HTML
        tabela_html = df.to_html(
            classes='display compact nowrap',
            index=False,
            border=0,
            table_id='tabela-dados',
            header=True
        )

        # Gerar HTML estático
        with app.app_context():
            html = render_template('index.html', tabela=tabela_html)
            os.makedirs('docs', exist_ok=True)
            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(html)
        return True
    except Exception as e:
        print(f"Erro: {str(e)}")
        return False

if __name__ == '__main__':
    gerar_site_estatico()