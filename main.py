from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hi():
    return( render_template('main.html')
    )
if __name__ == "__main__":
    app.run(debug=True)