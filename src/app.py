from flask import Flask, request, jsonify
from bot import BhagavadGitaBot

app = Flask(__name__)
bot = BhagavadGitaBot()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to my Bhagavad Gita Bot!'})

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/get-response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    response = bot.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    # if app.config['FLASK_ENV'] == 'development':
    #     app.run(debug=True, host='0.0.0.0')
    # else:
    app.run(host='0.0.0.0')