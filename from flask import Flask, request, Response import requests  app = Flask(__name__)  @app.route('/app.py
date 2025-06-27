from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/download')
def download():
    file_id = request.args.get('id')
    if not file_id:
        return "Missing file ID", 400
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    with requests.get(url, stream=True) as r:
        def generate():
            for chunk in r.iter_content(chunk_size=8192):
                yield chunk
        return Response(generate(), content_type=r.headers.get('Content-Type'))
