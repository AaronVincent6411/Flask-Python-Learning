from flask import Flask

app =  Flask(__name__)

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is a fish</h2>'


@app.route('/profile/<username>')
def profile(username):
    return '<h2>This is %s</h2>' % username

@app.route('/post/<int:post_id>')
def Id(post_id):
    return '<h2>Post Id= %s</h2>'  % post_id

if __name__ == '__main__':
    app.run(debug=True)