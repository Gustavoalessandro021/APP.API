from flask import Flask, request, render_template

app = Flask(__name__)
def index():
    return render_template("index.html")

@app.route("/soma/<valor1>/<valor2>")
@app.route("/subtrair/valor1/valor2")
@app.route("/multiplicar/valor1/valor2")
@app.route("/divisao/valor1/valor2")
def izaque():
    return 'soma/valor1=5/valor2=6'

if __name__ == "__main__":
    app.run(debug=True)