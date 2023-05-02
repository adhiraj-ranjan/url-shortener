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
        else:
            if extras.has_illegal_characters(alias):
                return jsonify({"status": "fail", "response": "Some Special Chars are Not Allowed"})
        if api.create_route(alias, long_url):
            return jsonify({"status": "ok", "response": "route is created", "url": f'https://{request.host}/{alias}'})
        else:
            return jsonify({"status": "fail", "response": "This Alias is Not Availaible"})
    else:
        return jsonify({"status": "fail", "response": "URL is Invalid"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'url.png', mimetype='image/vnd.microsoft.icon')

@app.route("/admin/cleanup_database")
def cleanup():
    return api.perform_cleanup()

@app.route('/manifest.json')
def web_manifest():
    return app.send_static_file("manifest.json")
    
@app.route('/<path:value>')
def re_route(value):
    url = api.get_redirection_url(value)
    if url:
        return redirect(url)
    else:
        return jsonify({"status": "not found"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)
