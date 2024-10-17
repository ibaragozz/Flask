from flask import Flask, render_template

app = Flask(__name__)




@app.route('/')
def html():

    return render_template('index.html')



if __name__ == '__main__':
    app.run()