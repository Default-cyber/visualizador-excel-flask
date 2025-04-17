from flask import Flask, render_template
import pandas as pd
import os

# Inicializa o app Flask (usado só para render_template aqui)
app = Flask(__name__)

def gerar_site_estatico():
    try:
        # Caminhos dos arquivos
        caminho_excel = os.path.join('data', 'dados.xlsx')
        caminho_saida = os.path.join('docs', 'index.html')

        # Carrega os dados do Excel
        df = pd.read_excel(caminho_excel)
        df = df.fillna('')  # Substitui NaNs por strings vazias

        # Converte para HTML (DataTables com opções certas)
        tabela_html = df.to_html(
            classes='display compact nowrap',
            index=False,
            border=0,
            table_id='tabela-dados',
            header=True,
            escape=False  # Permite HTML dentro das células, útil para ícones etc
        )

        # Gera o HTML final usando o template index.html
        with app.app_context():
            html_renderizado = render_template('index.html', tabela=tabela_html)

            # Cria pasta se não existir
            os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

            # Salva o HTML no diretório docs/
            with open(caminho_saida, 'w', encoding='utf-8') as f:
                f.write(html_renderizado)

        print(f"✅ HTML gerado com sucesso em: {caminho_saida}")
        return True

    except Exception as e:
        print(f"❌ Erro ao gerar o site: {str(e)}")
        return False

if __name__ == '__main__':
    gerar_site_estatico()
