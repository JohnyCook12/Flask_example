from flask import Flask, render_template, url_for, redirect, request, session, flash
from datetime import timedelta
app = Flask(__name__)


# ===============================================================================================
# ========================================    FORMS    ==========================================
# ===============================================================================================


# ====================  LOGIN FORM (POST method)  ====================
"""Simple form. Reading form input as dict key. Then go to profile page based on dynamic url (url_for)"""

@app.route('/')
def home():
    return 'Simple Homepage'


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



# ====================  LOGIN FORM - SESSION  ====================
"""Login using session. Name from /login_s/ form is stored in session DICT and checked on profile page.
Session is closed when you close browser. Or session can be permanent for some time."""

app.secret_key = 'some_secret_string'                           # NECESSARY !! for sessions
app.permanent_session_lifetime = timedelta(minutes=5)           # session lasts for 5 min after closing browser

@app.route('/login_s/', methods=['GET','POST'])                # chooses reaction based on method
def login_s():
    if request.method=='POST':
        session.permanent = True
        user = request.form['nm']                           # request.form[] reads variables as keys of dict
        session['user'] = user                              # create SESSION with dict key 'user'
        return redirect(url_for('user_s'))                  # profile page is static now.
    else:
        if 'user' in session:                               # if logged in -> profile. Else -> login page
            return redirect(url_for('user_s'))
        else:
            return render_template('form_login.html')


@app.route('/ses/user/')
def user_s():
    if 'user' in session:
        user = session['user']
        flash('You have been logged in!', 'info')           # flash message
        return render_template('user_page.html', user_in_html = user)
    else:
        return redirect(url_for('login_s'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        flash('You have been logged out!', 'info')              # flash message
    session.pop('user', None)                               # None is just a message when you pop out from dict.
    return redirect(url_for('login_s'))

# =====================================================
# ========================== RUN ======================
if __name__ == '__main__':
    app.run(debug=True)