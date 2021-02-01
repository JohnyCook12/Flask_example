from flask import Flask, url_for, render_template
app = Flask(__name__)                   # default function is app. Name = this file name

@app.route('/')                         # defines route (url) of index.
def index():
    return 'Hello from Flask!'


my_age = 32
@app.route('/osobni/')                               # route 1
@app.route('/personal/')                             # route 2 (for same page)
def pers():
    return f'Hello.     Name: Johny Cook, city: Prague, Age: {my_age}'



username = 'Johny'                                     # DYNAMIC ROUTEs:
@app.route(f'/user/<username>/')                       # var in format /<variable>/
def profile(username):

    return f'This is infopage about user {username}:'



@app.route('/url/')                                     # GENERATE URL
def show_url():
    return url_for('profile', username='hroncok')       # First arg = name of function that generate dynamic route. Second arg = argument required in d. route.




@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

