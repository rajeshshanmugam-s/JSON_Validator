import flask as flk
import json
import requests

app = flk.Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    return "Working"


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raw_json = flk.request.form.get('text', "default text")
        valid_json = json.loads(raw_json)
    except ValueError:
        result = "Not a valid Json"
        return flk.render_template('index.html', results=result)
    return flk.render_template('index.html', results=valid_json)


if __name__ == "__main__":
    app.run(debug=True)


