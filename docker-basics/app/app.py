# A simple web app using Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker-1!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
