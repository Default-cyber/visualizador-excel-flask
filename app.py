from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)


def gerar_site_estatico():
    try:
        caminho_excel = os.path.join('data', 'dados.xlsx')
        caminho_saida = os.path.join('docs', 'index.html')

        if not os.path.exists(caminho_excel):
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_excel}")

        # Processamento dos dados
        df = pd.read_excel(caminho_excel)
        df.fillna('-', inplace=True)
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        # Geração da tabela
        tabela_html = df.to_html(
            classes='data-table',
            index=False,
            border=0,
            na_rep='-'
        )

        # Geração do HTML
        with app.app_context():
            html = render_template('index.html', tabela=tabela_html)
            os.makedirs('docs', exist_ok=True)

            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(html)

            print("✅ Site gerado com sucesso!")
            return True

    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False


if __name__ == '__main__':
    if gerar_site_estatico():
        print("Acesse o site em: docs/index.html")
    else:
        print("Corrija os erros antes de continuar")