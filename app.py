import os
import base64
import io
from flask import Flask,render_template,request,send_file
import requests
import oyaml as yaml
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml'), Loader=yaml.FullLoader)

    return render_template('index.html', data=website_data)


@app.route('/speech', methods=['POST'])
def speech():
    url = "https://joj-text-to-speech.p.rapidapi.com/"

    text = request.form['text']

    payload = {
        "input": { "text": text },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-News-L",
            "ssmlGender": "FEMALE"
        },
        "audioConfig": { "audioEncoding": "MP3" }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "joj-text-to-speech.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers).json()

    response = response['audioContent']
    
    decoded_content = base64.b64decode(response)
    
    file = io.BytesIO(decoded_content)
    file.seek(0)

    return send_file(file, mimetype='audio/mp3')


@app.route('/download', methods=['POST'])
def download():
    url = "https://joj-text-to-speech.p.rapidapi.com/"

    text = request.form['text']

    payload = {
        "input": { "text": text },
        "voice": {
            "languageCode": "en-US",
            "name": "en-US-News-L",
            "ssmlGender": "FEMALE"
        },
        "audioConfig": { "audioEncoding": "MP3" }
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.environ.get('API_KEY'),
        "X-RapidAPI-Host": "joj-text-to-speech.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers).json()

    response = response['audioContent']
    
    decoded_content = base64.b64decode(response)
    
    file = io.BytesIO(decoded_content)
    file.seek(0)

    return send_file(file, mimetype='audio/mp3', as_attachment=True,download_name='speech.mp3')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


