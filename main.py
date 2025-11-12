from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")
@app.route('/soma/<valor1>/<valo>')



def dc(valor1,valor):
    soma = f"{valor1 + valor}"
    return f'o {valor1}com o {valor} deu a soma de {soma}'
@app.route('/subtraçao/<valor2>/<valor>')



def pc(valor2,valor):
    subtraçao = f"{valor2 - valor}"
    return f'o {valor2} com o {valor} deu a subtraçao{subtraçao}'
@app.route('/multiplicaçao/<valor3>/<valor>')



def tc(valor3,valor):
    multiplicaçao = f"{valor3 * valor}"
    return f'o{valor3}com o {valor} deu a multiplicaçao{multiplicaçao}'
@app.route('/divisão/<valor4>/<valor>')



def hc(valor4,valor):
    divisão = f"{valor4 / valor}"
    if valor4 == 0:
        print ("coloque um numero valido")
    elif valorrrrr == 0:
        print("coloque um numero valido")
    else:
        return f'o {valor4}com o {valor} deu a divisão{divisão}'


if __name__ =="__main__":
    app.run(debug=True)
