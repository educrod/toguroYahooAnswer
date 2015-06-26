from flask import Flask, jsonify
from utils import GoogleSearch, GetBestAnswer
import os

app = Flask(__name__)

@app.route('/search')
@app.route('/search/<query>')
def search(query):
    question = GoogleSearch(query)
    baseret = [{"GsearchResultClass": "Erro: Tente outra busca",  "unescapedUrl": "Erro: Tente outra busca",  "url": "Erro: Tente outra busca",
                "visibleUrl": "Erro: Tente outra busca",  "cacheUrl": "Erro: Tente outra busca",  "title": "Erro: Tente outra busca",  "titleNoFormatting": "Erro: Tente outra busca",  "content": "Erro: Tente outra busca"}]

    if question['responseData']['results']:
        q = question['responseData']['results'][0]
        res = GetBestAnswer(q['unescapedUrl'])

        for _ in baseret[0]:
            baseret[0][_] = res

        ret = {}
        ret['results'] = baseret
        return jsonify(responseData=ret)
    else:
        return jsonify(responseData=baseret)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
