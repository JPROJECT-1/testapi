from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    val = data.get("val")
    
    if val is None:
        return jsonify({"error": "Missing 'val' in request"}), 400
    
    return jsonify({"val": val < 10})

def handler(event, context):
    return app(event, context)
