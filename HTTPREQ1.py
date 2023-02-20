from flask import Flask, request

app = Flask(__name__)

@app.route('/')

def index():
    return '<h2>You are using method: %s</h2>' % request.method

@app.route('/bacon', methods = ['GET','POST'])
def bacon():
    if request.method == 'POST':
        return '<h2>You are using POST method</h2>' 
    else:
        return '<h2>You are using GET method</h2>' 
    
if __name__ == '__main__':
    app.run()