from flask import Flask,request,jsonify
from flask_cors import CORS
import recomm

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
        
@app.route('/api/recc/<book>')
def recommend_movies(book):
        res = recomm.predict_score(book)
        print(res)
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)
