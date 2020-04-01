import flask
app = flask.Flask(__name__)

@app.route('/', methods=["GET"])
def get_articles():
  size = flask.request.args.get("size", default=10, type=int)
  page = flask.request.args.get("page", default=0, type=int)
  if size < 0 or page < 0:
    context = {
      "message": "Bad Request",
      "status_code": 400
    }
    return (flask.jsonify(**context), 400)
  offset = size * page
  context = {
    'results': []
  }
  return flask.jsonify(**context)