from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render! I'm alive."

@app.route('/health')
def health():
    return {"status": "ok", "env": os.environ.get("ENV", "dev")}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
