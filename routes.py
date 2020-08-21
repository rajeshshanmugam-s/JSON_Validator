import flask as flk

app = flk.Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def test():
    return "Working"

if __name__ == "__main__":
    app.run()


