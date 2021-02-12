from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'some_secret_string'                               # NECESSARY !! for sessions
app.permanent_session_lifetime = timedelta(minutes=5)               # session lasts for 5 min after closing browser
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'   # defines URI. users = name of table.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # optional (removes warnings)


# ===============================================================================================
# ========================================     SQL     ==========================================
# ===============================================================================================

db = SQLAlchemy(app)                    # associate DB with app

class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)              # ID column. 'id' = name of column. If missing, it takes name of the object (_id)
    name = db.Column(db.String(100))                                   # 100 = max.lenth (characters)
    email = db.Column(db.String(100))

    def __init__(self, name, email):                                # we give it names of variables. PRIMARY_KEY is created automatically
        self.name = name
        self.email = email


# ===============================================================================================
# ========================================    FORMS    ==========================================
# ===============================================================================================


# ====================  LOGIN FORM (POST method) - SIMPLE, no DB  ====================
"""Simple form. Reading form input as dict key. Then go to profile page based on dynamic url (url_for)"""

@app.route('/')
def home():
    return render_template('Home_page.html')


@app.route('/login/', methods=['GET','POST'])                # chooses reaction based on method
def login():
    if request.method=='POST':
        user = request.form['nm']                           # request.form[] reads variables as keys of dict
        return redirect(url_for('user', usr=user))
    else:
        return render_template('form_login.html')           # if GET


@app.route('/<usr>/')                                       # dynamic route for user page
def user(usr):
    return f'<h1>Hello {usr}</h1>'



# ====================  LOGIN FORM - SESSION + SQL  (ADVANCED)  ====================
"""Login using session. Name from /login_s/ form is stored in SESSION DICT and checked on profile page.
Session is closed when you close browser (or logout). Or session can be permanent for some time.

It flashes messages what happened (login / logout / save email)

user NAME and EMAIL is saved to  DB.
"""



@app.route('/login_s/', methods=['GET','POST'])                # chooses reaction based on method
def login_s():
    if request.method=='POST':
        session.permanent = True
        user = request.form['nm']                           # request.form[] reads variables as keys of dict
        session['user'] = user                              # create SESSION with dict key 'user'
        flash('Login succesful', 'info')                    # flash message. (info = type)

        found_user = users.query.filter_by(name=user).first()          # takes first object from DB with name=user
        if found_user:                                      # if user in DB
            session['email'] = found_user.email             # put his email info session

        else:                                               # user NOT in DB? -> CREATE user
            user_db_object = users(user, "")                # name=user, email=""
            db.session.add(user_db_object)                  # save to DB = add + commit
            db.session.commit()




        return redirect(url_for('user_s'))                  # profile page is static now.
    else:
        if 'user' in session:                               # if logged in -> profile. Else -> login page
            return redirect(url_for('user_s'))
        else:
            return render_template('form_login.html')


@app.route('/ses/user/', methods=['POST', 'GET'])
def user_s():
    email = None
    if 'user' in session:                                   # if user name in session (else -> login)
        user = session['user']

        if request.method == 'POST':                        # if POSTed email -> save email to SESSION and DB
            email = request.form['email_in_html']
            session['email'] = email

            found_user = users.query.filter_by(name=user).first()       # WRITEs email to DB
            found_user.email = email
            db.session.commit()

            flash('Email filled in', 'info')

        else:                                               # else -> GET
            if 'email' in session:                          # shows EMAIL if known
                email = session['email']
        return render_template('user_page.html', user_in_html = user, email_in_html = email)

    else:
        return redirect(url_for('login_s'))


@app.route('/view/')
def view():
    return render_template('view.html', values=users.query.all())


@app.route('/logout/')
def logout():
    if 'user' in session:
        flash('You have been logged out!', 'info')              # flash message
    session.pop('user', None)                               # None is just a message when you pop out from dict.
    session.pop('email', None)
    return redirect(url_for('login_s'))

# =====================================================
# ========================== RUN ======================
if __name__ == '__main__':
    db.create_all()                                     # create database
    app.run(debug=True)