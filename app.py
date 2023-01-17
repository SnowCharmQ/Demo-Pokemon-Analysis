from flask import *

import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/time')
def get_time():
    return utils.get_time()


if __name__ == '__main__':
    app.run()
