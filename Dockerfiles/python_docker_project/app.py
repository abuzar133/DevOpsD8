from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello,Devops students!! Welcome to Dockerized Python Application"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

