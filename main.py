import bottle
import spacy
import logging
import os

from json import dumps
from swagger_ui import api_doc


logging.info("Loading model..")
nlp = spacy.load("./models")
app = bottle.Bottle()
api_doc(
    app,
    config_path="./docs/specification.yml",
    url_prefix="/api/docs",
    title="API documentation",
)


@app.route("/api/intent")
def intent_inference():
    sentence = bottle.request.query["sentence"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "textcat"]
    with nlp.disable_pipes(*other_pipes):
        inference = nlp(sentence)
    bottle.response.content_type = "application/json"
    return dumps(inference.cats)


@app.route("/api/intent-supported-languages")
def supported_languages() -> str:
    bottle.response.content_type = "application/json"
    return dumps(["fr-FR"])


@app.route("/api/health")
def health_check_endpoint() -> bottle.HTTPResponse:
    return bottle.HTTPResponse(status=200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    bottle.run(app, host="0.0.0.0", port=port, debug=True, reloader=True)
