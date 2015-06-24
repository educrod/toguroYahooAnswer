from flask import Flask, jsonify
from unidecode import unidecode
from utils import GoogleSearch, GetBestAnswer
import os

app = Flask(__name__)

@app.route('/search')
@app.route('/search/<query>')
def search(query):
    question = GoogleSearch(query)
    q = question['responseData']['results'][0]
    res = GetBestAnswer(q['unescapedUrl'])
#    return "%s\n%s" % (unidecode(q['title']), res)
    return jsonify(bestanswer=res)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
