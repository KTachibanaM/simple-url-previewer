import logging
from flask import Flask, request, jsonify
from .simple_url_previewer import Previewer, PreviewError

previewer = Previewer()

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return "Simple URL Previewer"


@app.route('/api', methods=["GET"])
def api():
    request_json = request.get_json(force=True, silent=True)
    if not request_json:
        return jsonify({
            "status": "error",
            "error_message": "payload is not a JSON"
        }), 400
    if 'url' not in request_json:
        return jsonify({
            "status": "error",
            "error_message": "url is not in JSON payload"
        }), 400
    url = request_json['url']
    if type(url) != str:
        return jsonify({
            "status": "error",
            "error_message": "url is not a string"
        }), 400

    try:
        preview = previewer.preview(url)
        return jsonify({
            "status": "ok",
            "payload": {}  # TODO
        })
    except PreviewError as pe:
        return jsonify({
            "status": "error",
            "error_message": pe.message
        }), 400
    except Exception as e:
        logging.error(e)
        return jsonify({
            "status": "error",
            "error_message": "unknown error"
        }), 500


if __name__ == '__main__':
    app.run()
