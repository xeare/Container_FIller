from flask import Flask, request, render_template

from container_filler import ContainerFiller


app = Flask(__name__)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
# above allows me to use break and continue in jinja


@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        result = str(
            ContainerFiller().calculate(int(request.form['teaspoons'])))
        return render_template('gallons.html', value=result)
    except ValueError:
        return render_template('ValueErrorException.html')
    except Exception as e:
        return '<html> <p> %s </p> </html>' % e


if __name__ == '__main__':
    app.run(debug=True)

# FLASK_APP=service.py python3 -m flask run
