


from flask import Flask, url_for, render_template, request
from flask_restful import Resource, Api
app = Flask(__name__)

def abort(chyba):
    return "Error: ", 400

@app.errorhandler(400)
def spatny_pozadavek(chyba):
    return "Tohle nejde počítat", 400


@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('calc.html')
    elif request.method == "POST":
        print(request.form)
        try:
            prvni_cislo = int(request.form["prvni"])
            druhe_cislo = int(request.form["druhe"])
        except ValueError:
            abort(400)
            return render_template('vysledek.html', zobrazeny_vysledek='Chyba. ValueError')


        operace = request.form["operace"]

        if operace == 'plus':
            vysledek = prvni_cislo+druhe_cislo
        if operace == 'minus':
            vysledek = prvni_cislo-druhe_cislo
        if operace == 'krat':
            vysledek = prvni_cislo*druhe_cislo
        if operace == 'deleno':
            vysledek = prvni_cislo/druhe_cislo

        return vysledek_page(vysledek)


@app.route('/vysledek/')
def vysledek_page(cislo):
    return render_template('vysledek.html', zobrazeny_vysledek=str(cislo))




# ========================== RUN ======================
if __name__ == '__main__':
    app.run(debug=True)