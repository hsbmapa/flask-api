from flask import Flask, jsonify, request

api = Flask(__name__)

@api.route('/health')
def health():
    return "Success"

@api.route('/math', methods=['POST'])
def math():
    num = None
    limit = 10000000
    req_data = request.get_json()
    if 'num' not in req_data:
        return "Invalid JSON", 400
    try:
        num = int(req_data['num'])
        result = num*1337
        if result > limit:
            return "Returned value higher than 10,000,000", 400
        return jsonify({"result": result})
    except:
        return "Input value not an integer", 400

if __name__ == '__main__':
    api.run(host= '0.0.0.0',debug=True)