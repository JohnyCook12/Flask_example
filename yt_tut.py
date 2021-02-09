from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


# ====================  TEMPLATE  ====================
@app.route('/author/')
def author():
    return render_template('author.html')



# ====================  TEMPLATE  ====================
@app.route('/visitor/')
def visitor():
    return render_template('visitor.html')



# ====================  TEMPLATE (index.html) + variable  ====================

message = '<h1>Chapter one:<h1> Street was covered in snow'        # HTML doesnt work here! (auto-escaping)
name_list = ['Anna', 'Bella', 'Ciri', 'Dana']                      # + for loop, if loop in HTML

@app.route('/')
def home():
    return render_template('index.html', content = message, content2 = name_list)



# ====================  Dynamic route  ====================
@app.route('/<name>/')
def hello_user(name):
    return f'Good morning Mr. {name}'



# ====================  url_for, redirect  ====================
@app.route('/something/')                                               # this url redirects you to homepage
def some_function():
    return redirect(url_for('home'))







# ========================== RUN ======================
if __name__ == '__main__':
    app.run(debug=True)