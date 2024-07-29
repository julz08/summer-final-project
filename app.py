from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/about-me')
def aboutme():
    return render_template("about-me.html")

@app.route('/archive-vids')
def archivevid():
    return render_template("wip.html")

@app.route('/archive-media')
def archivemedia():
    return render_template("wip.html")

@app.route('/archive-github')
def archivegithub():
    return render_template("wip.html")

@app.route('/review-manga')
def reviewmanga():
    return render_template("wip.html")

@app.route('/review-webtoons')
def reviewwebtoons():
    return render_template("wip.html")

@app.route('/review-manhwa')
def reviewmanhwa():
    return render_template("wip.html")

@app.route('/review-books')
def reviewbooks():
    return render_template("wip.html")

@app.route('/review-shows')
def reviewshows():
    return render_template("wip.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)