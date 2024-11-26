import requests
from flask import Flask, render_template, request

app = Flask(__name__)


API_URL = "https://translate.googleapis.com/translate_a/single"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    source_language = request.form.get('source_language')
    target_language = request.form.get('target_language')


    params = {
        'client': 'gtx',
        'sl': source_language,
        'tl': target_language,
        'dt': 't',
        'q': text
    }

    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        translation = response.json()[0][0][0]
        return render_template(
            'index.html',
            original_text=text,
            translated_text=translation,
            source_language=source_language,
            target_language=target_language
        )
    else:
        return render_template(
            'index.html',
            error="Erro ao realizar a tradução. Verifique os dados e tente novamente."
        )

if __name__ == '__main__':
    app.run(debug=True)
