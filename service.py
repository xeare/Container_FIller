from flask import Flask, request, render_template

from container_filler import ContainerFiller

app = Flask(__name__)

@app.route('/submit')
def submit_display():
    return render_template('index.html')
