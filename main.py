from flask import Flask, render_template, request, jsonify, redirect, send_from_directory
from utils import extras
from utils import api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_short_url', methods=['POST'])
def shorten_url():
    long_url = request.json['long_url']
    alias = request.json['alias']

    if extras.is_valid_url(long_url):
        if not alias:
            alias = extras.get_string()
        if api.create_route(alias, long_url):
            return jsonify({"status": "ok", "response": "route is created", "url": f'{request.scheme}://{request.host}/{alias}'})
        else:
            return jsonify({"status": "fail", "response": "THIS ALIAS IS NOT AVAILABLE"})
    else:
        return jsonify({"status": "fail", "response": "URL IS INVALID"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'url.png', mimetype='image/vnd.microsoft.icon')


@app.route('/<path:value>')
def re_route(value):
    url = api.get_redirection_url(value)
    if url:
        return redirect(url)
    else:
        return jsonify({"status": "not found"})



if __name__ == '__main__':
    app.run(debug=True)
