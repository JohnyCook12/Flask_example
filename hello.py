from flask import Flask, url_for, render_template
app = Flask(__name__)                                   # default run function is app. Name = this file name

@app.route('/')                                         # url of index.
def index():
    return f'Hello from Flask!.....URL pro index: {url_for("pers")}'


my_age = 32
@app.route('/osobni')                                   # route 1
@app.route('/personal/')                                # route 2 (for same page)
@app.route('/pers_info')                               # route 3
def pers():
    return f'Hello! Name: Johny, city: Prague, Age: {my_age}'



username = 'Johny'                                     # DYNAMIC ROUTEs:
@app.route(f'/user/<username>/')                       # var in format <variable>
def profile(username):
    return f'This is infopage about user {username}:'



@app.route('/url/')                                     # GENERATE URL
def show_url():
    return url_for('profile', username='hroncok')       # First arg = name of function that generate dynamic route. Second arg = argument required in d. route.




@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)     # loads from TEMPLATES folder

# print('URL pro index:',url_for('index')
# print('URL pro pers:',url_for('pers'))
# print('URL pro karluv profil:',url_for('profile', 'Karel'))