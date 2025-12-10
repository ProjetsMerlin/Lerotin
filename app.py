from method_1 import displayResult
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Appelle la fonction pour obtenir les données
    data = displayResult()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
