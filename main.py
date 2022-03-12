import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Решаем задачи!'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
