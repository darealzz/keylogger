from flask import (
    Flask, 
    request, 
    jsonify
)

app = Flask(__name__)

@app.route('/push_data')
def test():
    content = request.args.get("content", default="", type=str)
    client = request.args.get("client", defualt="", type=str)
, 
    return jsonify({"message": f"{client}"}), 200

app.run(host='0.0.0.0', port=8000, debug=True)
