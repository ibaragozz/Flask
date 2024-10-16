from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    caption = {
        'link' : 'Узнать больше'
    }
    return render_template('home.html', **caption)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()