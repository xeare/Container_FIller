from flask import Flask, request, render_template

from container_filler import ContainerFiller


app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return(
    '''
        <html><body><form action="http://localhost:5000/submit" method="POST">
        How many teaspoons of Moxie? <input type="text" name="teaspoons"/>
        <input type="submit"/></form><h1></h1></body></html>
        ''')

@app.route('/submit', methods=['POST'])
def submit():
    return str(ContainerFiller().calculate(int(request.form['teaspoons'])))

@app.route('/submit', methods=['GET'])
def submit_display():
    return render_template ('index.html')
