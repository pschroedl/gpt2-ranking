import os

from flask import Flask, request, send_file
from ranker import rank


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('index.html')
    context = request.form.get('context')
    response = request.form.get('response')
    return rank(context, response)


if __name__ == "__main__":
    app.run('0.0.0.0', os.environ.get('PORT', 8080), use_debugger=False, use_reloader=False, passthrough_errors=True)
