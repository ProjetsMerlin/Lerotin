from flask import Flask, render_template
from method_1 import method_1

app = Flask(__name__)
@app.route('/')
def index():
    data = method_1()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
