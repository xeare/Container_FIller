from flask import Flask, request, render_template

from container_filler import ContainerFiller


app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return str(ContainerFiller().calculate(int(request.form['teaspoons'])))
