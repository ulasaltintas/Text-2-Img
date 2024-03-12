from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__, static_url_path='/static')
client = OpenAI(api_key="YOUR TOKEN HERE")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt_text = request.form['text']
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_text,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return render_template('result.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
