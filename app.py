from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)


def gerar_site_estatico():
    try:
        # Carregar e processar dados
        df = pd.read_excel('data/dados.xlsx')
        df.fillna('-', inplace=True)

        # Converter para HTML com classes para filtragem
        tabela_html = df.to_html(
            classes='table table-striped table-bordered',
            index=False,
            border=0,
            na_rep='-',
            table_id='tabela-dados'
        )

        # Gerar arquivo estático
        with app.app_context():
            html = render_template('index.html', tabela=tabela_html)
            os.makedirs('docs', exist_ok=True)
            with open('docs/index.html', 'w', encoding='utf-8') as f:
                f.write(html)
        return True
    except Exception as e:
        print(f"Erro: {str(e)}")
        return False


if __name__ == '__main__':
    gerar_site_estatico()