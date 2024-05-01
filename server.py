from flask import Flask, request, jsonify
from models.title_generator import generateTitle, generate_title_v2
from models.summarizer import para_summarizer, para_summarize_v2
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, supports_credentials=True, allow_headers=["Content-Type"])


@app.post("/summarize-old")
@cross_origin()
def summarize():
    data = request.get_json(force=True)
    summarized_text = para_summarizer(data["text"])

    return jsonify({"summary": summarized_text})


@app.post("/summarize")
@cross_origin()
def summarize_v2():
    data = request.get_json(force=True)
    summarized_text = para_summarize_v2(data["text"])

    return jsonify({"summary": summarized_text})


@app.post("/generate-title")
@cross_origin()
def generate_title():
    data = request.get_json(force=True)
    title = generateTitle(data["text"])
    return jsonify({"title": title})


@app.post("/generate-title-v2")
@cross_origin()
def post_generate_title_v2():
    data = request.get_json(force=True)
    title = generate_title_v2(data["text"])
    return jsonify({"title": title})
