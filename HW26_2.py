from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def contacts():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
