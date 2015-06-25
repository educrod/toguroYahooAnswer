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
    ret = {}
    x = [{"GsearchResultClass": res, "unescapedUrl": res, "url": res,
	"visibleUrl": res, "cacheUrl": res, "title": res, "titleNoFormatting": res, "content": res}]
    ret['results'] = x
    return jsonify(responseData=ret)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
