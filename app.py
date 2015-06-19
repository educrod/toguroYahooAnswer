from flask import Flask, render_template
from utils import GoogleSearch, GetBestAnswer

app = Flask(__name__)

@app.route('/search')
@app.route('/search/<query>')
def search(query):
    question = GoogleSearch(query)
    q = question['responseData']['results'][0]
    res = GetBestAnswer(q['unescapedUrl'])
    return res

if __name__ == '__main__':
      app.run(debug=True)
