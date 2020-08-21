import flask as flk

app = flk.Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    return "Working"


@app.route('/', methods=['GET', 'POST'])
def index():
    return flk.render_template('index.html', results=flk.request.form['text'])


if __name__ == "__main__":
    app.run(debug=True)


