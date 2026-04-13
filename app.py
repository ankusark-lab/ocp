from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.getenv('HOSTNAME', 'Local-Machine')
    return f"<h1>Build Successful! Demo done new patch for uat</h1><p>Running on Pod: {pod_name}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3333)
