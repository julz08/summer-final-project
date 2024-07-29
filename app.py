from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/about-me')
def aboutme():
    return render_template("about-me.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)