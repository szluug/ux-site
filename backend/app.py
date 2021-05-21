from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hoo')
def hello_world2():
    return render_template('hello.html', name='Patryk i Kuba')

if __name__ == '__main__':
    app.run(debug=True)
