from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User Agent')
    return '<h2> Your browser is {}</h2>'.format(user_agent)

if __name__ == '__main__':
    app.run(debug=True)